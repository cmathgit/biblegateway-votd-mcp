# BibleGateway Verse of the Day MCP Server

This is a MCP server for the BibleGateway Verse of the Day Web Service: NO API Key Required

#Example VOTD URL KJV ID: 9
```
https://www.biblegateway.com/votd/get/?format=JSON&version=9
```

[BibleGateway VOTD Documentation](https://www.biblegateway.com/share/#versehtml)

For a list of all the versions and their IDs, see:
[Version List](https://www.biblegateway.com/usage/linking/versionslist/)

## Installation: use guide by [Model Context Protocol Quickstart: For Server Developers](https://modelcontextprotocol.io/quickstart/server) which uses [uv](https://docs.astral.sh/uv/getting-started/installation/) instead of pip. Cloning this repo will download all scripts each with a set langauge. If these are not needed, feel free to delete. The primary script is biblegateway-votd.py. biblegateway-votd-basic.py has most relevant English translations.
```
git clone https://github.com/cmathgit/biblegateway-votd-mcp.git
cd biblegateway-votd-mcp
# Create virtual environment and activate it
uv venv
.venv\Scripts\activate
# Install dependencies
uv add mcp[cli] httpx
```
#Feel free to test each of the servers by running them with uv
```
uv run biblegateway-votd.py
```

#Before adding any of the servers to the MCP configuration, be selective about which languages you add. biblegateway-votd.py has some versions that I use primarily. Feel free to add/replace any versions from the other languages that you think you'll need in this file. Please refer to the [Version List](https://www.biblegateway.com/usage/linking/versionslist/) for a list of all the versions and their IDs. I created servers for every version and language available, so you can obtain those via the GitHub repo history. Some IDEs such as Cursor will limit the number of tools that can be added to the global context. There are many languages covered by the BibleGateway VOTD, and thus many tools, so be sure to only add the versions you need. Some Plugins such as Cline and Roo Code allow Project scoped context, so you can add all the tools and only use the ones you need for a specific project.

#Add the servers to the MCP, include this configuration in your IDEs mcp json config file. Roo code, Cline, Gemini-CLI, and Cursor have an MCP servers settings menu with a "Configure MCP Servers" button that will open the mcp.json file in your IDE. Claude Desktop Developer Configuation is standard and works perfectly fine. Cursor is known to limit the combined length of the server name and tool name to 60 characters. I am working to resolve an issue with Cline, but the tools seem to work even though the server lists an error. Roo Code sems to handle the server well.
```
{
    "mcpServers": {
        "biblegateway-votd": {
            "command": "/ABSOLUTE/PATH/TO/PARENT/FOLDER/uv",
            "args": [
                "--directory",
                "/ABSOLUTE/PATH/TO/PARENT/FOLDER/biblegateway-votd-mcp",
                "run",
                "biblegateway-votd.py"
            ]
        }
    }
}
```

#This configuration assumes that you will use only the primary script, biblegateway-votd.py. To use the other scripts in this repo, swap out the name of the file. It is highly recommended to use only a few tools at time due to context limitations and tool number restrictions. Personally, I swap out the tools in these files with the primary script as needed.
```
biblegateway-votd-basic.py
biblegateway-votd-alternate-languages.py
biblegateway-votd-english.py
biblegateway-votd-greek.py
biblegateway-votd-chinese.py
biblegateway-votd-russian.py
biblegateway-votd-french.py
biblegateway-votd-german.py
biblegateway-votd-italian.py
biblegateway-votd-japanese.py
biblegateway-votd-portugues.py
biblegateway-votd-spanish.py
biblegateway-votd-deutsch.py
biblegateway-votd-dutch.py
biblegateway-votd-tagalog.py
biblegateway-votd-svenska.py
biblegateway-votd-bulgarian.py
```

#To use the MCP in your agent, simple ask for the VOTD in the language/bible version of your choice.
Nueva Versión Internacional bible
```
What is the verse of the day in the Nueva Versión Internacional bible?
```
Contemporary English Version
```
What is the verse of the day in the Contemporary English Version
```
New International Version (by ID #)
```
What is the verse of the day in the bible version with ID: 31
```
Gujarati: પવિત્ર બાઈબલ (Pavitra Baibal) or Holy Bible 
```
What is the verse of the day in the bible version with ID: 278
```
Gujarati: પવિત્ર બાઈબલ (Pavitra Baibal) or Holy Bible (by ID # 278)
```
What is the verse of the day in the પવિત્ર બાઈબલ (Pavitra Baibal) or Hindi Holy Bible
```
Bengali: পবিত্র বাইবেল (Pobitro Bible) or Holy Bible (by ID # 289)
```
What is the verse of the day in the pobitro bible
```

# You may need to tweak the tool names to fit your IDE's context length limit, but I find the ID # works well. Refer to Version List to find the ID # for the version you want: [Version List](https://www.biblegateway.com/usage/linking/versionslist/).

