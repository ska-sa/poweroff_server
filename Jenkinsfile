#!groovy

@Library('katsdpjenkins') _
katsdp.killOldJobs()
katsdp.setDependencies(['ska-sa/katsdpdockerbase/master'])
katsdp.standardBuild(push_external: true)
katsdp.mail('sdpdev+poweroff_server@ska.ac.za')
