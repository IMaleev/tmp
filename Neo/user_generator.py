import pyodbc

user_name = 'SRavulapati'

base_path = "c:\\src\\vsts\\UsersUpdate\\UsersUpdate\\runAfterOtherAnyTimeScripts\\"

request_user_id = "SELECT UserId FROM [SECURITY].[User] WHERE UserName='{0}'"
request_user_data = "SELECT [UserName],[Password],[AllClients],[AllLabs],[PasswordQuestion],[PasswordAnswer]," \
               "[Approved],[Lockedout],[Online]," \
               "convert(nvarchar(MAX), [LastLoginDate], 21) AS LastLoginDate," \
               "convert(nvarchar(MAX), [LastActivityDate], 21) AS LastActivityDate," \
               "convert(nvarchar(MAX), [LastPasswordChangeDate], 21) AS LastPasswordChangeDate," \
               "convert(nvarchar(MAX), [LastLockoutDate], 21) AS LastLockoutDate," \
               "[Active]," \
               "convert(nvarchar(MAX), [CreatedDate], 21) AS CreatedDate," \
               "[CreatedUserID],[CreatedSystemID]," \
               "convert(nvarchar(MAX), [ModifiedDate], 21) AS ModifiedDate," \
               "[ModifiedUserID],[ModifiedSystemID],[SignatureImageID],[HomeLabID]," \
               "convert(nvarchar(MAX), [UserAgreeDate], 21) AS UserAgreeDate," \
               "[WorklistOptions]," \
               "convert(nvarchar(MAX), [LastUnlockDate], 21) AS LastUnlockDate," \
               "[AllStates],[InternalEmployee] FROM [SECURITY].[User] WHERE UserId='{0}' "
request_person_id = "SELECT PersonId FROM [SECURITY].[User] WHERE UserId={0}"
request_person_data = "SELECT [LastName], [FirstName], [MiddleName], [Credential], [SocialSecurityNo], " \
                      "convert(nvarchar(MAX), [DateOfBirth], 21) AS DateOfBirth," \
                      "[Gender], [Ethnicity], [EmailAddress], [Active], " \
                      "convert(nvarchar(MAX), [CreatedDate], 21) AS CreatedDate," \
                      "[CreatedUserID], [CreatedSystemID], " \
                      "convert(nvarchar(MAX), [ModifiedDate], 21) AS ModifiedDate," \
                      "[ModifiedUserID], [ModifiedSystemID], [MaritalStatus], [Suffix], [SearchFirstName], " \
                      "[SearchLastName] FROM [ORDERS].[Person] WHERE PersonId={0}"
request_user_role = "SELECT [RoleID], [Active], " \
                    "convert(nvarchar(MAX), [CreatedDate], 21) AS CreatedDate," \
                    "[CreatedUserID], [CreatedSystemID], " \
                    "convert(nvarchar(MAX), [ModifiedDate], 21) AS ModifiedDate," \
                    "[ModifiedUserID], [ModifiedSystemID], [IsDefault]" \
                    "FROM [APvX].[SECURITY].[UserRole] WHERE userId={0}"
request_user_feature = "SELECT [FeatureID], [Grant], [Active], " \
                       "convert(nvarchar(MAX), [CreatedDate], 21) AS CreatedDate," \
                       "[CreatedUserID], [CreatedSystemID], " \
                       "convert(nvarchar(MAX), [ModifiedDate], 21) AS ModifiedDate," \
                       "[ModifiedUserID], [ModifiedSystemID] " \
                       "FROM [APvX].[SECURITY].[UserFeature] WHERE userId={0}"
request_user_lab = "SELECT [LabID], [Active], " \
                   "convert(nvarchar(MAX), [CreatedDate], 21) AS CreatedDate," \
                   "[CreatedUserID], [CreatedSystemID], " \
                   "convert(nvarchar(MAX), [ModifiedDate], 21) AS ModifiedDate," \
                   "[ModifiedUserID], [ModifiedSystemID] FROM [APvX].[SECURITY].[UserLab] WHERE userId={0}"
request_user_landing_page = "SELECT [WebPageID], [Active], " \
                            "convert(nvarchar(MAX), [CreatedDate], 21) AS CreatedDate," \
                            "[CreatedUserID], [CreatedSystemID], " \
                            "convert(nvarchar(MAX), [ModifiedDate], 21) AS ModifiedDate," \
                            "[ModifiedUserID], [ModifiedSystemID] " \
                            "FROM [APvX].[WORKFLOW].[UserLandingPage] WHERE userId={0}"
request_user_worklist_column = "SELECT [WorklistColumnID], [Sort], [Link], [Active], [CreatedUserID], " \
                               "convert(nvarchar(MAX), [CreatedDate], 21) AS CreatedDate," \
                               "[ModifiedUserID], " \
                               "convert(nvarchar(MAX), [ModifiedDate], 21) AS ModifiedDate," \
                               "[DefaultSort], [ASC] " \
                               "FROM [APvX].[WORKFLOW].[UserWorklistColumn] WHERE userId={0}"
request_user_client = "SELECT [ClientID], [Active], " \
                      "convert(nvarchar(MAX), [CreatedDate], 21) AS CreatedDate," \
                      "[CreatedUserID], [CreatedSystemID], " \
                      "convert(nvarchar(MAX), [ModifiedDate], 21) AS ModifiedDate," \
                      "[ModifiedUserID], [ModifiedSystemID] FROM [APvX].[SECURITY].[UserClient] WHERE userId={0}"
request_user_department = "SELECT [DepartmentID], [Active], " \
                          "convert(nvarchar(MAX), [CreatedDate], 21) AS CreatedDate, " \
                          "[CreatedUserID], " \
                          "convert(nvarchar(MAX), [ModifiedDate], 21) AS ModifiedDate, " \
                          "[ModifiedUserID] FROM [APvX].[UserManagement].[UserDepartment] WHERE userId={0}"

connection = pyodbc.connect('DRIVER={SQL Server};SERVER=fm1dvm-nlis01;DATABASE=APvX;UID=test;PWD=test')
cursor = connection.cursor()


def get_user_id(user_name):
    cursor.execute(request_user_id.format(user_name))
    row = cursor.fetchone()
    return row.UserId


def get_user(user_id):
    cursor.execute(request_user_data.format(user_id))
    row = cursor.fetchone()
    return row


def get_user_role(user_id):
    cursor.execute(request_user_role.format(user_id))
    rows = []
    while True:
        row = cursor.fetchone()
        if row:
            rows.append(row)
        else:
            return rows


def get_user_feature(user_id):
    cursor.execute(request_user_feature.format(user_id))
    rows = []
    while True:
        row = cursor.fetchone()
        if row:
            rows.append(row)
        else:
            return rows


def get_user_lab(user_id):
    cursor.execute(request_user_lab.format(user_id))
    rows = []
    while True:
        row = cursor.fetchone()
        if row:
            rows.append(row)
        else:
            return rows


def get_user_landing_page(user_id):
    cursor.execute(request_user_landing_page.format(user_id))
    rows = []
    while True:
        row = cursor.fetchone()
        if row:
            rows.append(row)
        else:
            return rows


def get_user_worklist_column(user_id):
    cursor.execute(request_user_worklist_column.format(user_id))
    rows = []
    while True:
        row = cursor.fetchone()
        if row:
            rows.append(row)
        else:
            return rows


def get_user_client(user_id):
    cursor.execute(request_user_client.format(user_id))
    rows = []
    while True:
        row = cursor.fetchone()
        if row:
            rows.append(row)
        else:
            return rows


def get_user_department(user_id):
    cursor.execute(request_user_department.format(user_id))
    rows = []
    while True:
        row = cursor.fetchone()
        if row:
            rows.append(row)
        else:
            return rows


def get_person_id(user_id):
    cursor.execute(request_person_id.format(user_id))
    row = cursor.fetchone()
    return row.PersonId


def get_person(person_id):
    cursor.execute(request_person_data.format(person_id))
    row = cursor.fetchone()
    return row


def itemToString(item):
    if item is None:
        return "NULL"
    # if isinstance(item, bool):
    #     return "'{0}'".format(str(item))
    if isinstance(item, bool):
        return "{0}".format(int(item))
    if isinstance(item, str):
        return "'{0}'".format(str(item))
    return item


def generate_insert_user(data):
    items = list(map(itemToString, data))
    return "\tINSERT INTO [APvX].[SECURITY].[User]([PersonID],[UserName],[Password],[AllClients],[AllLabs],[PasswordQuestion],[PasswordAnswer],[Approved],[Lockedout],[Online],[LastLoginDate],[LastActivityDate],[LastPasswordChangeDate],[LastLockoutDate],[Active],[CreatedDate],[CreatedUserID],[CreatedSystemID],[ModifiedDate],[ModifiedUserID],[ModifiedSystemID],[SignatureImageID],[HomeLabID],[UserAgreeDate],[WorklistOptions],[LastUnlockDate],[AllStates],[InternalEmployee])\n" \
           "\tVALUES (@personId, {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}, {23}, {24}, {25}, {26});"\
        .format(*items)


def generate_insert_person(data):
    items = list(map(itemToString, data))
    return "\tINSERT INTO [APvX].[ORDERS].[Person]([LastName], [FirstName], [MiddleName], [Credential], [SocialSecurityNo], [DateOfBirth], [Gender], [Ethnicity], [EmailAddress], [Active], [CreatedDate], [CreatedUserID], [CreatedSystemID], [ModifiedDate], [ModifiedUserID], [ModifiedSystemID], [MaritalStatus], [Suffix], [SearchFirstName], [SearchLastName])\n" \
           "\tVALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19});"\
        .format(*items)


def generate_insert_user_role(data):
    if len(data) == 0:
        return ""
    role_entries = []
    for data_entry in data:
        items = list(map(itemToString, data_entry))
        role_entry = "(@userId, {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8})".format(*items)
        role_entries.append(role_entry)
    result = ",\n\t".join(role_entries)
    return "\tINSERT INTO [APvX].[SECURITY].[UserRole]( [UserID], [RoleID], [Active], [CreatedDate], [CreatedUserID], [CreatedSystemID], [ModifiedDate], [ModifiedUserID], [ModifiedSystemID], [IsDefault])\n" \
           "\tVALUES {0};".format(result)


def generate_insert_user_feature(data):
    if len(data) == 0:
        return ""
    feature_entries = []
    for data_entry in data:
        items = list(map(itemToString, data_entry))
        feature_entry = "(@userId, {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8})".format(*items)
        feature_entries.append(feature_entry)
    result = ",\n\t".join(feature_entries)
    return "\tINSERT INTO [APvX].[SECURITY].[UserFeature]([UserID], [FeatureID], [Grant], [Active], [CreatedDate], [CreatedUserID], [CreatedSystemID], [ModifiedDate], [ModifiedUserID], [ModifiedSystemID])\n" \
           "\tVALUES {0};".format(result)


def generate_insert_user_lab(data):
    if len(data) == 0:
        return ""
    lab_entries = []
    for data_entry in data:
        items = list(map(itemToString, data_entry))
        lab_entry = "(@userId, {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7})".format(*items)
        lab_entries.append(lab_entry)
    result = ",\n\t".join(lab_entries)
    return "\tINSERT INTO [APvX].[SECURITY].[UserLab]([UserID], [LabID], [Active], [CreatedDate], [CreatedUserID], [CreatedSystemID], [ModifiedDate], [ModifiedUserID], [ModifiedSystemID])\n" \
           "\tVALUES {0};".format(result)


def generate_insert_user_landing_page(data):
    if len(data) == 0:
        return ""
    page_entries = []
    for data_entry in data:
        items = list(map(itemToString, data_entry))
        page_entry = "(@userId, {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7})".format(*items)
        page_entries.append(page_entry)
    result = ",\n\t".join(page_entries)
    return "\tINSERT INTO [APvX].[WORKFLOW].[UserLandingPage]([UserID], [WebPageID], [Active], [CreatedDate], [CreatedUserID], [CreatedSystemID], [ModifiedDate], [ModifiedUserID], [ModifiedSystemID])\n" \
           "\tVALUES {0};".format(result)


def generate_insert_user_worklist_column(data):
    if len(data) == 0:
        return ""
    column_entries = []
    for data_entry in data:
        items = list(map(itemToString, data_entry))
        column_entry = "(@userId, {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9})".format(*items)
        column_entries.append(column_entry)
    result = ",\n\t".join(column_entries)
    return "\tINSERT INTO [APvX].[WORKFLOW].[UserWorklistColumn]([UserID], [WorklistColumnID], [Sort], [Link], [Active], [CreatedUserID], [CreatedDate], [ModifiedUserID], [ModifiedDate], [DefaultSort], [ASC])\n" \
           "\tVALUES {0};".format(result)


def generate_insert_user_client(data):
    if len(data) == 0:
        return ""
    client_entries = []
    for data_entry in data:
        items = list(map(itemToString, data_entry))
        client_entry = "(@userId, {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7})".format(*items)
        client_entries.append(client_entry)
    result = ",\n\t".join(client_entries)
    return "\tINSERT INTO [APvX].[SECURITY].[UserClient]([UserID],[ClientID],[Active],[CreatedDate],[CreatedUserID],[CreatedSystemID],[ModifiedDate],[ModifiedUserID],[ModifiedSystemID])\n" \
           "\tVALUES {0};".format(result)


def generate_insert_user_department(data):
    if len(data) == 0:
        return ""
    department_entries = []
    for data_entry in data:
        items = list(map(itemToString, data_entry))
        department_entry = "(@userId, {0}, {1}, {2}, {3}, {4}, {5})".format(*items)
        department_entries.append(department_entry)
    result = ",\n\t".join(department_entries)
    return "\tINSERT INTO [APvX].[UserManagement].[UserDepartment]([UserID],[DepartmentID],[Active],[CreatedDate],[CreatedUserID],[ModifiedDate],[ModifiedUserID])\n" \
           "\tVALUES {0};".format(result)


def generate_header():
    return "IF NOT EXISTS (SELECT * FROM [APvX].[SECURITY].[User] WHERE UserName='{0}')\n" \
           "BEGIN".format(user_name)


def generate_footer(password):
    return "END\n" \
           "GO\n\n" \
           "UPDATE [APvx].[SECURITY].[User]\n" \
           "SET LockedOut = 0,\n" \
           "\tLastLockoutDate = NULL,\n" \
           "\tLastPasswordChangeDate = GETDATE()-1,\n" \
           "\tPassword = '{0}'\n" \
           "WHERE UserName = '{1}'\n" \
           "GO".format(password, user_name)


def generate_person_id_declaration(data):
    return "\tDECLARE @personId Int;\n" \
           "\tSET @personId = (SELECT PersonId FROM [APvX].[ORDERS].[Person] WHERE LastName='{0}' AND FirstName='{1}' AND EmailAddress='{2}');".format(data.LastName, data.FirstName, data.EmailAddress)


def generate_user_id_declaration():
    return "\tDECLARE @userId Int;\n" \
           "\tSET @userId = (SELECT UserId FROM [APvX].[SECURITY].[User] WHERE UserName='{0}');".format(user_name)


def main():
    filename = "{0}.EVERYTIME.sql".format(user_name)
    user_id = get_user_id(user_name)
    user_data = get_user(user_id)
    password = user_data.Password
    person_id = get_person_id(user_id)
    person_data = get_person(person_id)
    user_role_data = get_user_role(user_id)
    user_feature_data = get_user_feature(user_id)
    user_lab_data = get_user_lab(user_id)
    user_landing_page_data = get_user_landing_page(user_id)
    user_worklist_column_data = get_user_worklist_column(user_id)
    user_client_data = get_user_client(user_id)
    user_department = get_user_department(user_id)

    with open(base_path+filename, 'w') as f:
        print(generate_header(), "\n",
              generate_insert_person(person_data), "\n\n",
              generate_person_id_declaration(person_data), "\n\n",
              generate_insert_user(user_data), "\n\n",
              generate_user_id_declaration(), "\n\n",
              generate_insert_user_role(user_role_data), "\n\n",
              generate_insert_user_feature(user_feature_data), "\n\n",
              generate_insert_user_lab(user_lab_data), "\n\n",
              generate_insert_user_landing_page(user_landing_page_data), "\n\n",
              generate_insert_user_worklist_column(user_worklist_column_data), "\n\n",
              generate_insert_user_client(user_client_data), "\n\n",
              generate_insert_user_department(user_department),
              "\n"+generate_footer(password),
              file=f)


main()
