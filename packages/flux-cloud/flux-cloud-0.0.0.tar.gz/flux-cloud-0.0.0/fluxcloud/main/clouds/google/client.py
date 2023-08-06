# Copyright 2022 Lawrence Livermore National Security, LLC and other
# This is part of Flux Framework. See the COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

import copy
import os
import shutil

import fluxcloud.utils as utils
from fluxcloud.logger import logger
from fluxcloud.main.client import ExperimentClient


class GoogleCloud(ExperimentClient):
    """
    A Google Cloud GKE experiment runner.
    """

    name = "google"

    def __init__(self, **kwargs):
        super(GoogleCloud, self).__init__(settings_file=kwargs.get("settings_file"))
        self.zone = kwargs.get("zone") or "us-central1-a"
        self.project = kwargs.get("project") or self.settings.google["project"]

        # No project, no go
        if not self.project:
            raise ValueError(
                "Please provide your Google Cloud project in your settings.yml or flux-cloud set google:project <project>"
            )

    def apply(self, setup, force=False):
        """
        Apply a CRD to run the experiment and wait for output.

        This is really just running the setup!
        """
        # Here is where we need a template!
        if not setup.template or not os.path.exists(setup.template):
            logger.exit(
                "You cannot run experiments without a minicluster-template.yaml"
            )
        apply_script = self.get_script("minicluster-run")

        results = []
        for experiment in setup.matrices:

            # Save times on the level of the experiment
            times = {}

            # One run per job (command)
            jobs = experiment.get("jobs", [])
            minicluster = setup.get_minicluster(experiment)
            if not jobs:
                logger.warning(f"Experiment {experiment} has no jobs, nothing to run.")
                continue

            # The experiment is defined by the machine type and size
            experiment_prefix = "%s-%s" % (experiment["machine"], experiment["size"])
            experiment_dir = os.path.join(setup.outdir, experiment_prefix)

            # Jobname is used for output
            for jobname, job in jobs.items():

                # Job specific output directory
                job_output = os.path.join(experiment_dir, jobname)
                logfile = os.path.join(job_output, "log.out")

                # Do we have output?
                if os.path.exists(logfile) and not force:
                    logger.warning(
                        f"{logfile} already exists and force is False, skipping."
                    )
                    continue
                elif os.path.exists(logfile) and force:
                    logger.warning(f"Cleaning up previous run in {job_output}.")
                    shutil.rmtree(job_output)

                # Create job directory anew
                utils.mkdir_p(job_output)

                # Generate the populated crd from the template
                template = setup.generate_crd(experiment, job)

                # Write to a temporary file
                crd = utils.get_tmpfile(prefix="minicluster-", suffix=".yaml")
                utils.write_file(template, crd)

                # Apply the job, and save to output directory
                cmd = [
                    apply_script,
                    "--apply",
                    crd,
                    "--logfile",
                    logfile,
                    "--namespace",
                    minicluster["namespace"],
                    "--job",
                    minicluster["name"],
                ]
                self.run_timed_append(f"minicluster-run-{jobname}", cmd, times)

                # Clean up temporary crd if we get here
                if os.path.exists(crd):
                    os.remove(crd)

            # Save times to file
            # TODO we could add cost estimation here - data from cloud select
            meta = copy.deepcopy(experiment)
            times.update(self.times)
            meta["times"] = times
            results.append(meta)

        meta_file = os.path.join(setup.outdir, "meta.json")
        utils.write_json(results, meta_file)

    def up(self, setup):
        """
        Bring up a cluster
        """
        experiment = setup.get_single_experiment()
        create_script = self.get_script("cluster-create")
        tags = setup.get_tags(experiment)

        # Create the cluster with creation script
        cmd = [
            create_script,
            "--project",
            self.project,
            "--zone",
            self.zone,
            "--machine",
            setup.get_machine(experiment),
            "--cluster",
            setup.get_cluster_name(experiment),
            "--cluster-version",
            setup.settings.kubernetes["version"],
            "--size",
            setup.get_size(experiment),
        ]
        if tags:
            cmd += ["--tags", ",".join(tags)]
        return self.run_timed("create-cluster", cmd)

    def down(self, setup):
        """
        Destroy a cluster
        """
        experiment = setup.get_single_experiment()
        destroy_script = self.get_script("cluster-destroy")

        # Create the cluster with creation script
        return self.run_timed(
            "destroy-cluster",
            [
                destroy_script,
                "--zone",
                self.zone,
                "--cluster",
                setup.get_cluster_name(experiment),
            ],
        )
