"""
  @Project     : sentry-dingtalks
  @Time        : 2022/05/26 15:35:12
  @File        : plugin.py
  @Author      : source
  @Software    : VSCode
  @Desc        :
"""


import requests
import six
import ast
import random
from sentry import tagstore
from sentry.plugins.bases import notify
from sentry.utils import json
from sentry.utils.http import absolute_uri
from sentry.integrations import FeatureDescription, IntegrationFeatures
from sentry_plugins.base import CorePluginMixin
from django.conf import settings
class DingTalkPluginS(CorePluginMixin, notify.NotificationPlugin):
    title = "DingTalkS"
    slug = "dingtalks"
    description = "Post notifications to Dingtalk."
    conf_key = "dingtalks"
    required_field = "webhook"
    author = "source"
    author_url = "https://xxx.xxx.cc/FE/sentry-k8s/-/tree/main/sentry-dingtalks"
    version = "1.0.1"
    resource_links = [
        ("Report Issue", "https://xxx.xxx.cc/FE/sentry-k8s/-/tree/main/sentry-dingtalks/issues"),
        ("View Source", "https://xxx.xxx.cc/FE/sentry-k8s/-/tree/main/sentry-dingtalks"),
    ]

    feature_descriptions = [
        FeatureDescription(
            """
                钉钉通知 可配置对应告警人 仅支持钉钉ID 用于查看用户信息.
                """,
            IntegrationFeatures.ALERT_RULE,
        )
    ]

    def is_configured(self, project):
        return bool(self.get_option("webhook", project))

    def get_config(self, project, **kwargs):
        return [
            {
                "name": "webhook",
                "label": "webhook",
                "type": "url",
                "placeholder": "https://oapi.dingtalks.com/robot/send?access_token=**********",
                "required": True,
                "help": "钉钉 webhook 支持@成员",
                "default": self.set_default(project, "webhook", "DINGTALK_WEBHOOK"),
            },
            {
                "name": "project_user",
                "label": "project_user",
                "type": "string",
                "placeholder": "钉钉id,逗号分隔多个",
                "required": True,
                "help": "项目对应负责人",
                "default": self.set_default(
                    project, "project_user", ""
                ),
            }
        ]

    def set_default(self, project, option, env_var):
        if self.get_option(option, project) != None:
            return self.get_option(option, project)
        if hasattr(settings, env_var):
            return six.text_type(getattr(settings, env_var))
        return None

    def notify(self, notification, raise_exception=False):
        event = notification.event
        release = event.release
        group = event.group
        project = group.project
        tagsUrl = event.get_tag('url')
        minimalUser = event.get_minimal_user()
        userMsg = minimalUser.__dict__
        self._post(group, release, project,tagsUrl,userMsg)

    def _post(self, group, release, project,tagsUrl,userMsg):
        webhook = self.get_option("webhook", project)
        userPhone = {
            "robb":"kmac007",
            "xavierluo":"7wo-42z112tyr",
            "junjianlin":"wnkmxo4",
            "wendylin":"lqcforest",
            "Ryanzeng":"3s5-c0c4fx2sf",
            "harleyhong":"hongyan2000",
            "jielu":"jiezi1997fe",
            "sallyhuang":"1y1-2pjc0lhyq7",
            "ininitluo":"ok20zf7",
            "yulu":"tlc34ah",
            "yinanchen":"drw_yylgku2gj",
            "davoschen":"cdd112160",
            "solomon":"qbv98if",
            "fengzegui":"p1g_825zmi8hr",
            "yinglichen":"wzd_symai5lil",
            "jackzhao":"et4g7pw",
            "vitoliu":"1ib-cbgwbz5qvx",
            "snicker":"qpk1zjk",
            "Nicolasyan":"1nh-8c10onrv31",
            "ianchen":"ekp4fgw",
            "Holyhe":"14c-0a9i5co67z",
            "andyyang":"lipgw3v",
            "sourceliu":"lydaniel",
            "emily":"ij5wx65",
            "Shirleychen":"wtdu423",
            "Olivechen":"1fm-otwfuw2m8o",
            "linalu":"1gc-v9xnvmpjb7",
            "perrysong":"turingmaster",
            "vickwang":"uen6zu6",
            "violetguo":"1ij-fxndksqxkt",
            "hanzhao":"cnwmm9x"
        }
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title":""
            }
        }
        headers = {
            "Content-type": "application/json",
            "Accept": "text/plain",
            "charset": "utf8"
        }
        issue_link = group.get_absolute_url(params={"referrer": "dingtalks"})
        print(issue_link)
        assignee = group.get_assignee()
        tips_list = ["tags中的release的信息对应的是gitlab的commitid前十位,可以用release快速定位问题的产生版本","善用sourcemap、vue上下文信息来快速定位问题","异常难以定位？考虑在业务中加入面包屑补充场景试试","指定解决版本 避免问题的频繁骚扰"]
        if assignee != None:
            userId = userPhone[assignee.name]
            tips = random.choice(tips_list)
            print(userId)
            payload = f"#### [让人头大]已指派的问题还未解决，用户再次触发，请核查\n\n"
            payload = f"{payload} #### 项目名：{project.name}\n\n"
            payload = f"{payload} #### 问题处理人：[@{assignee.name}](dingtalk://dingtalkclient/action/sendmsg?dingtalk_id={userId})\n\n"
            payload = f"{payload} #### [异常信息]({issue_link}): \n\n"
            payload = f"{payload} > {group.message}…\n\n"
            payload = f"{payload} > userMsg:{userMsg['_data']}\n\n"
            payload = f"{payload} > {tagsUrl}\n\n"
            payload = f"{payload} ###### 小提示：{tips}\n\n"
            data['markdown']["title"] = f"{project.name}问题被重新激活,问题地址：{issue_link}"
            data["at"]={
                "atDingtalkIds": userId.split(","),
                "isAtAll": "false"
            }
        else:
            # 项目负责人
            project_user = self.get_option("project_user", project)
            user_list = project_user.split(",")
            ats_ding_str = ""
            for at in user_list:
                ats_ding_str = f"{ats_ding_str} [@{at}](dingtalk://dingtalkclient/action/sendmsg?dingtalk_id={at})"
            payload = f"### 「[打叉] 前端监控告警」\n\n"
            payload = f"{payload} #### 项目名：{project.name}\n\n"
            payload = f"{payload} #### 跟进人：{ats_ding_str}\n\n"
            payload = f"{payload} #### 版本：{release} \n\n"
            payload = f"{payload} #### [异常信息]({issue_link}): \n\n"
            payload = f"{payload} > {group.message}…\n\n"
            payload = f"{payload} > userMsg:{userMsg['_data']}\n\n"
            payload = f"{payload} > {tagsUrl}\n\n"
            payload = f"{payload} ###### [客服]请项目负责人及时查看分配处理\n\n"
            data['markdown']["title"] = f"{project.name}发生告警,问题地址：{issue_link}"
            data["at"]={
                "atDingtalkIds": user_list,
                "isAtAll": "false"
            }
        data['markdown']["text"] = payload
        print(data)
        requests.post(webhook, data=json.dumps(data), headers=headers)
        print(userMsg['_data'])
