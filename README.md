# DreamingRock

![gitDream](https://github.com/studioHEX/DreamingRock/assets/159900742/3f318ec2-7084-4da5-8b49-7557d8997492)


DreaminRock is an art project that tries to let a rock dream about it's heritage through video and audio. In the Netherlands we have a bunch of rocks that landed here from scandinavia during the last ice age. I always found it mezmerizing that the rocks are already so old and been used in various ritualistic neolithic burial sites while they are actually way older than that and perhaps also had some function in their native homelands. 

In order to make the rocks dream about their heritage I am using stylegan3 and a mixture of YAMNet, audio classification network and a custom RNN to predict audio events based on the probability build on the YAMNet classifications. The RNN network is currently being build. 

The artwork will be a generative installation where an ESP32 with ECG-sensor is being used to control the realtime latent space traversal in Stylegan and imported into TouchDesigner. In the current build the texture is imported through screen grab but a system on python 3.10 Spout is being researched. 

In the repo you can find the custom Stylegan3 network that imports OSC and makes realtime latent space traversal based on the Visualizer.py script. There are also the custom YAMNet scripts as well as a webscraper script with a Resizer script to build a suitable dataset for Stylegan3 made by John Ottenlip.

In May I will travel to Norway to build up a custom visual and audio dataset which I will also share in this repo. 
