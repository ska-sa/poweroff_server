#!groovy

@Library('katsdpjenkins') _
katsdp.killOldJobs()
katsdp.setDependencies(['ska-sa/katsdpdockerbase/master'])
katsdp.standardBuild(python3: true, python2: false, push_external: true)
katsdp.mail('sdpdev+poweroff_server@ska.ac.za')
