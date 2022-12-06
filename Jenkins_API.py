import jenkins



client = jenkins.Jenkins("http://localhost:8080", username="johnthomsonn", password="password")

#client.build_job('Run_Multiple_Tests')

#client.build_job('Run_Single_Test', {"Test_To_Run":"PTP/set_cmcc5g.py", "ip":"100g-vm1"})


xml = """<?xml version='1.1' encoding='UTF-8'?>
<project>
  <builders>
    <hudson.tasks.Shell>
      <command>echo this is testing!</command>
    </hudson.tasks.Shell>
  </builders>
</project>"""

#new_job = client.create_job('api', jenkins.EMPTY_CONFIG_XML)
new_job = client.create_job('apid', xml)


#client.build_job(new_job)