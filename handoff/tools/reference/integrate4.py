import re
F='/home/user/hello-world/nc_medicaid_bh_dashboard.html'
t=open(F).read()
def rep(old,new,count=1):
    global t
    assert t.count(old)>=1,old[:60]
    t=t.replace(old,new,count)
rep("The sources conflict: the Governor's September 30, 2026 release limits the first RHIF round to primary care, FQHCs, community health centers and certain safety-net providers, while ncbroadband.gov lists behavioral health providers. Email RHIF@nc.gov before you apply.",
    "Year 1 of the RHIF is limited to primary care providers, FQHCs, community health centers and qualifying safety-net providers (Governor's release, September 30, 2026). A new SAIOP, SACOT or peer support provider probably does not qualify yet. Email RHIF@nc.gov to confirm before you spend time on the application.")
rep("Settle the conflict over first-round RHIF eligibility with RHIF@nc.gov.",
    "Year 1 RHIF eligibility is limited to primary care and safety-net providers; confirm with RHIF@nc.gov whether behavioral health providers qualify. No regional NC ROOTS grant was open on October 18, 2026: the Trillium Region 2 and 5 rounds were closed, UNC was still developing its process, and Access East had posted none.")
rep("Review the Rural Health Innovation Fund: complete","Review the Rural Health Innovation Fund (year 1 is limited to primary care and safety-net providers): complete")
rep("so there are three Tailored Plan regions, not four.","so there are three Tailored Plans, not four.")
rep("Alliance cites Senate Bill 257 effective July 2, 2026.","Alliance and Trillium cite July 2, 2026, which is the day the General Assembly ratified Senate Bill 257. The section took effect when the Governor approved it on July 7, so use July 7.")
rep("Accepted bodies are COA, The Joint Commission and CARF.","Accepted bodies are COA, The Joint Commission and CARF; the Aug 16, 2026 matrix also lists CQL, which the April bulletin does not.")
rep("Ask the Ombudsman which date NCTracks enforces, and plan to the earlier date.","Ask the Ombudsman (866-304-7062) or the NCTracks Call Center (800-688-6696) for a written answer on which date NCTracks enforces, and plan to the earlier date. Also ask whether CQL is accepted: the Aug 16, 2026 matrix lists it but the April bulletin does not.")
# steps 14-16 are DHSR licensure: SAIOP and SACOT only
for n in (14,15,16):
    i=t.index("stepNumber: 'Step %d'"%n)
    j=t.index("services: ['8G', '8A-12', '8A-13']",i)
    assert j-i<400
    t=t[:j]+"services: ['8A-12', '8A-13']"+t[j+len("services: ['8G', '8A-12', '8A-13']"):]
rep("Peer support only: the NCTracks Provider Permission Matrix (Aug 16, 2026) does not require a DHSR license for peer support, but whether it is licensable at your site is unconfirmed, so call DHSR at 919-855-3795 before skipping licensure.",
    "This step applies to SAIOP and SACOT. Peer support does not need a DHSR license: DHSR's Feb 10, 2026 new-provider presentation lists it among services it does not license, and the Aug 16, 2026 Provider Permission Matrix shows no license required.")
open(F,'w').write(t); print('ok')
