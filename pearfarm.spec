<?php

$spec = Pearfarm_PackageSpec::create(array(Pearfarm_PackageSpec::OPT_BASEDIR => dirname(__FILE__)))
             ->setName('phrocco')
             ->setChannel('oneblackbear.pearfarm.org')
             ->setSummary('A PHP port of Docco')
             ->setDescription('Now you can have beautiful looking annotated source files for your PHP projects')
             ->setReleaseVersion('0.2.5')
             ->setReleaseStability('beta')
             ->setApiVersion('0.2.4')
             ->setApiStability('beta')
             ->setLicense(Pearfarm_PackageSpec::LICENSE_MIT)
             ->setNotes('Initial release.')
             ->addMaintainer('lead', 'Ross Riley', 'rossriley', 'ross@oneblackbear.com')
             ->addGitFiles("http://github.com/oneblackbear/phrocco")
             ->addExcludeFiles(array('.gitignore', '.git', 'pearfarm.spec'))
             ->addExecutable('bin/phrocco')
             ;