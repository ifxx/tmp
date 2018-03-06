#!/usr/bin/env 
#coding=utf-8
from wxpy import *
import jenkins
from time import sleep

jenkins_server_url='http://ssncg.koreacentral.cloudapp.azure.com:8080'
#在用户设定中找到uid 和 token
user_id=''
api_token=''
server = jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)
jobOn = 'testOn'
jobOff = 'testOff'

def run_jenkins_job(jobname):
    next_build_number = server.get_job_info(jobname)['nextBuildNumber']
    server.build_job(jobname)
    sleep(2)
# 返回执行结果
    return server.get_build_info(jobname, next_build_number)[u'result']

# 扫码登陆
bot = Bot(console_qr=True, cache_path=True)
# 初始化图灵机器人 (API key 申请: http://tuling123.com)
tuling = Tuling(api_key='aaaaaaaaaadddddddddddddddddddddkkkkkkkkkkkk')
# 自动回复所有文字消息
#gp=bot.groups().search('Roche vip')[0]
gp=ensure_one(bot.groups().search('Roche vip'))
@bot.register(gp)
#@bot.register()
def auto_reply_all(msg):
    if msg.text=='D:ON':
       msg.reply(u'已经为您处理')
       result=run_jenkins_job(jobOn)
       msg.reply(result)
       
    elif msg.text=='D:OFF':
       msg.reply(u'已经为您处理')
       result=run_jenkins_job(jobOff)
       msg.reply(result)
    else:
       tuling.do_reply(msg)


# 开始运行
bot.join()
