import json,re
f='/root/.claude/projects/-home-user-hello-world/91141d82-7be3-5ffc-bd0c-f501091745a6.jsonl'
EMAIL='user@example.com'
def red(s): return s.replace(EMAIL,'[user email redacted]')
turns=[]
def txt_of(c):
    if isinstance(c,str): return [c],[]
    ts=[];tools=[]
    for b in c:
        if not isinstance(b,dict): continue
        if b.get('type')=='text': ts.append(b['text'])
        elif b.get('type')=='tool_use':
            inp=json.dumps(b.get('input',{}),ensure_ascii=False)
            tools.append({'tool':b.get('name'),'input_preview':red(inp[:300])})
    return ts,tools
for l in open(f):
    try:o=json.loads(l)
    except: continue
    t=o.get('type')
    if t not in('user','assistant'): continue
    m=o.get('message',{})
    c=m.get('content')
    if c is None: continue
    ts,tools=txt_of(c)
    # drop tool_result-only user turns and pure system reminders
    keep=[]
    for x in ts:
        x2=re.sub(r'<system-reminder>.*?</system-reminder>','',x,flags=re.S).strip()
        if x2: keep.append(x2)
    if not keep and not tools: continue
    role=t
    kind='message'
    if t=='user':
        j=' '.join(keep)
        if j.startswith('[SYSTEM NOTIFICATION') or '<task-notification>' in j or 'Stop hook feedback' in j: kind='system_or_hook_notice'
        elif j.startswith('This session is being continued'): kind='compaction_summary'
        elif o.get('isMeta'): kind='meta'
    turns.append({'timestamp':o.get('timestamp'),'role':role,'kind':kind,'text':red('\n\n'.join(keep)),**({'tool_calls':tools} if tools else {})})
json.dump({'session_id':'91141d82-7be3-5ffc-bd0c-f501091745a6','note':'Verbatim user and assistant text from the Claude Code session, in order. Tool results are omitted (they are large); assistant tool calls are listed with a 300-character preview. System reminders are stripped. The raw session log is not included.','turns':turns},open('/tmp/transcript.json','w'),ensure_ascii=False,indent=1)
import collections
print(len(turns),collections.Counter((x['role'],x['kind']) for x in turns))
