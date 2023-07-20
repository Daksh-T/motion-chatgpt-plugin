# Motion Calendar ChatGPT Plugin

A ChatGPT plugin that uses the [Motion API](https://app.usemotion.com/) to interact with your 'Tasks' in natural language. This requires you to have plugin developer access as it runs on localhost. If you do not already have plugin developer access, please [join the waitlist](https://openai.com/waitlist/plugins).

## Setup
1. To install the required packages for this plugin, run:

```bash
pip install -r requirements.txt
```

2. Replace "YOUR MOTION API KEY" in `main.py` with your Motion API key. You can find your Motion API key by going to [https://app.usemotion.com/web/settings/api](https://app.usemotion.com/web/settings/api).

3. Then to start the main server, run:

```bash
python main.py
```

Once the local server is running:

1. Navigate to https://chat.openai.com. 
2. In the Model drop down, select "Plugins" (note, if you don't see it there, you don't have access yet).
3. Select "Plugin store"
4. Select "Develop your own plugin"
5. Enter in `localhost:5003` since this is the URL the server is running on locally, then select "Find manifest file".

The plugin should now be installed and enabled! You can start with a question like "What are my tasks?" and then try adding something to it as well! 

## How does it work?

The `main.py` script serves the manifest at `localhost:5003/.well-known/ai-plugin.json`, which contains a link to the `openapi.yaml` file on localhost (also served by the `main.py` script). Any request sent to the API is first received by localhost (without any auth) and then redirected to Motion with the auth token by `main.py`. The response is then sent back to the plugin.

## Disclaimer
The API response when asking for task list is very verbose and exceeds the model's context limit. This may cause it to hallucinate tasks.

## Feedback
Feel free to raise an Issue or submit a Pull Request if you have something to contibute to the project!

## Attribution
Parts of this project are taken from the [OpenAI Plugins Quickstart example](https://github.com/openai/plugins-quickstart). Thanks to the great folks at OpenAI for an easy-to-use template!

The plugin logo is taken from [Motion's website](https://app.usemotion.com/). I do not own the logo, all rights go to their respective owners.
