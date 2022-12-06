import jenkins



client = jenkins.Jenkins("http://localhost:8080", username="johnthomsonn", password="password")

#client.build_job('Run_Multiple_Tests')

#client.build_job('Run_Single_Test', {"Test_To_Run":"PTP/set_cmcc5g.py", "ip":"100g-vm1"})


xml2 = """<?xml version='1.1' encoding='UTF-8'?>
    <project>
    <actions/>
    <description>This can be used to run a single test</description>
    <keepDependencies>false</keepDependencies>
    <properties>
        <com.coravy.hudson.plugins.github.GithubProjectProperty plugin="github@1.36.0">
        <projectUrl>https://www.github.com/johnthomson-calnex/iTestMigrationTest/</projectUrl>
        <displayName/>
</com.coravy.hudson.plugins.github.GithubProjectProperty>
<hudson.model.ParametersDefinitionProperty>
<parameterDefinitions>
<hudson.model.StringParameterDefinition>
<name>Test_To_Run</name>
<description>This is the file of the test to run</description>
<trim>false</trim>
</hudson.model.StringParameterDefinition>
<hudson.model.StringParameterDefinition>
<name>ip</name>
<description>this is the unit ip</description>
<defaultValue>100g-vm1</defaultValue>
<trim>false</trim>
</hudson.model.StringParameterDefinition>
</parameterDefinitions>
</hudson.model.ParametersDefinitionProperty>
</properties>
<scm class="hudson.plugins.git.GitSCM" plugin="git@4.14.1">
<configVersion>2</configVersion>
<userRemoteConfigs>
<hudson.plugins.git.UserRemoteConfig>
<url>https://www.github.com/johnthomson-calnex/iTestMigrationTest.git</url>
</hudson.plugins.git.UserRemoteConfig>
</userRemoteConfigs>
<branches>
<hudson.plugins.git.BranchSpec>
<name>*/main</name>
</hudson.plugins.git.BranchSpec>
</branches>
<doGenerateSubmoduleConfigurations>false</doGenerateSubmoduleConfigurations>
<submoduleCfg class="empty-list"/>
<extensions/>
</scm>
<canRoam>true</canRoam>
<disabled>false</disabled>
<blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
<blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
<triggers/>
<concurrentBuild>false</concurrentBuild>
<builders>
<hudson.tasks.BatchFile>
<command>python %Test_To_Run% IF %ERRORLEVEL% EQU 0 (Echo The Test Passed!) ELSE (Echo The Test Failed)</command>
<configuredLocalRules/>
</hudson.tasks.BatchFile>
</builders>
<publishers/>
<buildWrappers>
<hudson.plugins.timestamper.TimestamperBuildWrapper plugin="timestamper@1.21"/>
</buildWrappers>
</project>
"""

#new_job = client.create_job('api', jenkins.EMPTY_CONFIG_XML)
new_job = client.create_job('api', xml2)

client.build_job('api', {"Test_To_Run":"set_ccsa.py"})




#client.build_job(new_job)




run_multiple_tests_config = """
<?xml version='1.1' encoding='UTF-8'?>
<flow-definition plugin="workflow-job@1254.v3f64639b_11dd">
  <actions>
    <org.jenkinsci.plugins.pipeline.modeldefinition.actions.DeclarativeJobAction plugin="pipeline-model-definition@2.2118.v31fd5b_9944b_5"/>
    <org.jenkinsci.plugins.pipeline.modeldefinition.actions.DeclarativeJobPropertyTrackerAction plugin="pipeline-model-definition@2.2118.v31fd5b_9944b_5">
      <jobProperties/>
      <triggers/>
      <parameters/>
      <options/>
    </org.jenkinsci.plugins.pipeline.modeldefinition.actions.DeclarativeJobPropertyTrackerAction>
  </actions>
  <description>This can be used to run multiple tests</description>
  <keepDependencies>false</keepDependencies>
  <properties/>
  <definition class="org.jenkinsci.plugins.workflow.cps.CpsScmFlowDefinition" plugin="workflow-cps@3536.vb_8a_6628079d5">
    <scm class="hudson.plugins.git.GitSCM" plugin="git@4.14.1">
      <configVersion>2</configVersion>
      <userRemoteConfigs>
        <hudson.plugins.git.UserRemoteConfig>
          <url>https://www.github.com/johnthomson-calnex/iTestMigrationTest.git</url>
        </hudson.plugins.git.UserRemoteConfig>
      </userRemoteConfigs>
      <branches>
        <hudson.plugins.git.BranchSpec>
          <name>*/main</name>
        </hudson.plugins.git.BranchSpec>
      </branches>
      <doGenerateSubmoduleConfigurations>false</doGenerateSubmoduleConfigurations>
      <submoduleCfg class="empty-list"/>
      <extensions/>
    </scm>
    <scriptPath>Jenkinsfile</scriptPath>
    <lightweight>true</lightweight>
  </definition>
  <triggers/>
  <disabled>false</disabled
"""