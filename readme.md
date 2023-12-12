Telegram Style Transfer bot
==============
---
This is study project of telegramm bot with stule transfer function with using Neural Style Transfer alghoritm.

***Contents:***
- [Project description](#Description)
- [Project setup](#Setup)
     - [Dependencies](#dependencies)
     - [Docker image](#docker)
     - [Tokens](#Tokens)
- [Working with Bot](#Bot)
     - [Commands](#Commands)
     - [Examples](#Samples)
 

# Project description <a name="Description"></a>

**Telegram Style Transfer bot** — This is study project of telegramm bot with stule transfer function with using Neural Style Transfer alghoritm.(NST). 
The main aim of the project is to create the working telegramm bot who can accept images and transform them. For transformation I used the ML-alghoritm NST (see link for details: https://pytorch.org/tutorials/advanced/neural_style_tutorial.html.)
  
# Project setup <a name="Setup"></a>

In project used Аiogram for bot anf PyThorch for ML-model. Python ver 3.10

## Dependencies <a name="dependencies"></a>

All needed dependencies described in `requarements.txt`.  
PyTorch versions used: `torch-2.0.0+cpu-cp310-cp310-win_amd64.whl`, and `torchvision-0.15.1+cpu-cp310-cp310-win_amd64.whl` avaible on PyTorch official website: https://download.pytorch.org/whl/cpu/torch_stable.html. You can also used another PyTorch version (>2.0.0) and CUDA, avaible on: https://pytorch.org/get-started/locally/

## Docker image<a name="docker"></a>

To create and run bot:
1. Add to the Dockerfile the bot token in `TG_BOT_TOKEN` in enviroment variable `ENV`:  
     `ENV TG_BOT_TOKEN 1234567`  
2. Create image using this command:
     `docker build -t bot .`
3. Run container:
     `docker run --name NST_bot -d bot`
4. Bot is running! First run may take some time, PyTorch will download models he needed.

## Tokens <a name="Tokens"></a>
  
Create file with enviroment variables `.env` and add bot token in variable `TG_BOT_TOKEN`.
Also in `config.config` in variable `ADMINS_ID` you can add administrator id to check the bot running (optional). 

  
# Working with Bot <a name="Bot"></a>

## Commands <a name="Commands"></a>

You can find all commands in keyboard. All other commands will have error message.
Commands list:
- `/start` - bot start
- `/help` - help
- `Style transfer` - stule transfer menu
     - `Load content image` - load content image
     - `Load style image` - load style image
     - `Back` - back to preveous menu/cancel
     - `Next` - next
- `Settings` - settings menu
     - `Set resolution` - set the image resolution
     - `Set iterations number` - set the alghorithm iterations
     - `Back` - back to preveous menu/cancel


## Examples <a name="Samples"></a>

Examples:
Go to transfer menu, load the content image and style image. Run the transfr process. It will be fast for low-resollution images:
![gif_1.gif](https://github.com/KononovichKiryll/TG_bot_Neural_Style_Transfer/blob/main/gif_screnshots/gif_1.gif)  
Till the process bot will be locked but answer the questions.  
  
  
You can set the resolution and the number of iterations befor start:  
![gif_2.gif](https://github.com/KononovichKiryll/TG_bot_Neural_Style_Transfer/blob/main/gif_screnshots/gif_2.gif)
  
Result:  
![attachment:Screenshot_4.png](https://github.com/KononovichKiryll/TG_bot_Neural_Style_Transfer/blob/main/gif_screnshots/Screenshot_4.png)
