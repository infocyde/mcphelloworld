Who, What, When, Where, Why

What:
This is just a hello world MCP server to get my feet wet, more advanced projects coming.

Why:
I've done tooling and used MCP servers but haven't written one.  I think it is trivial but I need to actually do it.

Link to MCP Repo:
https://github.com/modelcontextprotocol


**Basic Python**
I use pip, the cool kids are migrating to uv.  If you are a cool kid you will translate any differences to here.
1) In the folder of the repo, create a virtual environment (I'm using venv)
   Example command (run from a terminal window pointed at this directory): python - m venv .venv
   It might take a second.
2) Activate your virtual environment 
   .venv\scripts\active
3) run the requirments.txt file (run from directory)
   pip install -r requirements.txt    // optional --upgrade flag fyi


with pip or uv install "mcp[cli]" at the top of your python script or run the requirements file 


**Testing**
Note, you can get fancy in the testing, this is just to get you going.
In the main change the transport to "stdio" for now
run mcp dev [servername] // here it is mcpserver.py
It might want to install something, go ahead.
A web gui will pop up.
For Command put python, 
For Arguments, put [servername] //mcpserver.py
Hit connect, hopefully you are good.  
In the middle there is a tools button, click that to see toolds (methods) of your MCP server.  You can run test here.

**Grok vibe code thread** 
Grok thread that helped me out
https://grok.com/share/bGVnYWN5_d148735b-50d1-4c6e-8e1a-a4989866691b
