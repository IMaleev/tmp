from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication

personal_access_token = 'fmxcqfe3qe5axtpd556xivfl6irs5vomer544wbogdpjmvdrjraa'
organization_url = 'https://neogenomics.visualstudio.com/'
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

core_client = connection.clients.get_core_client()
neolink_project = core_client.get_project('NeoLink')

git_client = connection.clients.get_git_client()
apvx_repo = git_client.get_repository('APvX', neolink_project.id)

wit_client = connection.clients.get_work_item_tracking_client()


def delete_branch(branch_name):
    ref = git_client.get_refs(apvx_repo.id, neolink_project.id, "heads/"+branch_name)
    # print(ref.value[0])
    if ref.value[0].is_locked:
        # print(branch_name+" is locked by "+ref.value[0].is_locked_by)
        print(branch_name+" is locked")
    else:
        print("Deleting branch "+branch_name)
        ref_updates = [{"name": "refs/heads/"+branch_name,
                        "oldObjectId": ref.value[0].object_id,
                        "newObjectId": "0000000000000000000000000000000000000000"}]
        git_client.update_refs(ref_updates, apvx_repo.id, neolink_project.id)


def get_wi_state(wi_id):
    wi = wit_client.get_work_item(wi_id, neolink_project.id, fields=None, as_of=None, expand=None)
    if "Microsoft.VSTS.Common.ClosedDate" in wi.fields:
        return wi.fields["System.State"], wi.fields["Microsoft.VSTS.Common.ClosedDate"]
    else:
        return wi.fields["System.State"], None


def get_item_id(branch_name):
    item_id = branch_name.split('_')[0]
    if "/" in str(item_id):
        return item_id.split('/')[1]
    else:
        return int(item_id)


branches = git_client.get_branches(apvx_repo.id, neolink_project.id)
for branch in branches:
    if branch.is_base_version is not True:
        if branch.ahead_count == 0:
            delete_branch(branch.name)
            # pass
        else:
            try:
                item_id = get_item_id(branch.name)
                print(item_id, get_wi_state(item_id), branch.name)
            except:
                print(branch.name)
