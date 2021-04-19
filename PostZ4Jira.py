    for index in range(0,len(issueIDs)):
        if tcName.lower() == issueIDs[index]['name'].lower():
            return json.dumps(issueIDs[index]['issueID']).strip('\"')
    for index in range(0,len(issueIDs)):
        if similar(tcName.lower(), issueIDs[index]['name'].lower()) >= 0.80:
            return json.dumps(issueIDs[index]['issueID']).strip('\"')
    for index in range(0,len(issueIDs)):
        if tcName.lower() in issueIDs[index]['name'].lower():
            return json.dumps(issueIDs[index]['issueID']).strip('\"')
    for index in range(0,len(issueIDs)):
        if issueIDs[index]['name'].lower() in tcName.lower():
            return json.dumps(issueIDs[index]['issueID']).strip('\"')
    return 0
if __name__ == "__main__":
        ## constructor
        this = Jiphy("https://jira-eng-sjc14.cisco.com/rest/zapi/latest","jkarnati","Containity$15")

        ## constants
        projectID = this.get_projectID("Dragonfly")
        today = datetime.datetime.today().strftime('%d_%b_%y_%H%M%S')
        projectCode = "Dragonfly"
        versionName = "Dragonfly-1.3.x"
        versionID = this.get_versionID(projectID, versionName)
        #versionID = 123456789

        ## processors
        #cycleName = "AutoTest_" + str(today)
        cycleName = "Ad hoc"
        print("cycleName: " + cycleName)

        cycleID = this.get_test_cycleID(projectID, cycleName, versionID)
        issueIDs = this.get_all_issueID(projectCode)

        ## main iterator
        outputjson = this.parse_xml('output.xml')
        for result in range(0,len(outputjson)):
                for testname in range(0,len(outputjson[result])):
                        tcName = outputjson[result][testname]['name']
                        status = outputjson[result][testname]['status']
                        print(tcName + ": " + status)
                        issueID = Get_IssueID(issueIDs, tcName)
                        executionID = this.create_executionID(projectID, cycleID, issueID)
                        tries = 3
                        while True:
                                try:
                                        this.update_test_case_execution_status(executionID, status)
                                except:
                                        if tries > 0:
                                                tries -= 1
                                                continue
                                        else:
                                                raise
                                break
-- VISUAL LINE --                                                                                                                                         69,3-24       Bot
