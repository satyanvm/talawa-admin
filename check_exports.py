import subprocess
import re

exports = [
    "createAdSuccessMock", "infiniteScrollMocks", "MOCKS_ERROR_MUTATION",
    "MOCKS_ERROR", "REGISTRANTS_MOCKS_ERROR", "REACT_APP_CUSTOM_PORT",
    "MARK_CHECKOUT", "REGISTER_FOR_EVENT", "REGISTER_EVENT_ATTENDEE",
    "INVITE_EVENT_ATTENDEE", "UNREGISTER_FOR_EVENT_BY_USER",
    "ADDRESS_DETAILS_FRAGMENT", "UPDATE_USER_MUTATION", "ADD_MEMBER_MUTATION",
    "LIKE_POST", "UNLIKE_POST", "AgendaItemByOrganization",
    "GET_POSTS_BY_ORG", "FILTERED_ORGANIZATION_POSTS",
    "ORGANIZATION_ADMINS_LIST", "ORGANIZATION_FUNDS", "GET_PLUGIN_BY_ID",
    "ADVERTISEMENTS_GET", "USER_LIST_REQUEST", "GET_EVENT_ATTENDEE",
    "GET_EVENT_INVITES_BY_USER_ID", "HAS_SUBMITTED_FEEDBACK",
    "IS_USER_BLOCKED", "BLOCK_PAGE_MEMBER_LIST", "ADMIN_LIST",
    "GET_COMMUNITY_DATA", "EMPTY_MOCKS", "MOCKS3", "errorMock",
    "EDGE_CASE_MOCKS", "Role", "FilterPeriod", "hours",
    "mondayToFriday", "dayShortNames", "monthShortNames", "monthDays"
]

print("Checking exports for usage...")
print("=" * 80)

unused = []
used = []

for export_name in exports:
    result = subprocess.run(
        ["grep", "-rn", export_name, "src/", "--include=*.ts", "--include=*.tsx"],
        capture_output=True,
        text=True
    )
    
    lines = result.stdout.strip().split('\n') if result.stdout.strip() else []
    
    # Filter out definition lines
    usage_lines = [l for l in lines if l and not re.search(f'export (const|type|interface|let|var|enum) {export_name}', l)]
    
    print(f"\n{'='*80}")
    print(f"Export: {export_name}")
    print(f"{'='*80}")
    
    if len(usage_lines) == 0:
        unused.append(export_name)
        print(f"❌ UNUSED - Only definition found or not found at all")
        print("\nAll occurrences:")
        for line in lines:
            print(f"  {line}")
    else:
        used.append(export_name)
        print(f"✅ USED - Found {len(usage_lines)} usage(s)")
        print("\nAll occurrences:")
        for line in lines:
            if re.search(f'export (const|type|interface|let|var|enum) {export_name}', line):
                print(f"  [DEFINITION] {line}")
            else:
                print(f"  [USAGE] {line}")

print("\n" + "=" * 80)
print(f"\n📊 SUMMARY:")
print(f"=" * 80)
print(f"Unused: {len(unused)}")
print(f"Used: {len(used)}")
print(f"\n❌ SAFE TO DELETE:")
for item in unused:
    print(f"  - {item}")
print(f"\n✅ KEEP (used in code):")
for item in used:
    print(f"  - {item}")
