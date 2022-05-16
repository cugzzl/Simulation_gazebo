import rospy  # ros在python语言中的头文件
from std_msgs.msg import String  # 消息头文件

message = ''


def callback(data):
    global message
    message = data.data


if __name__ == '__main__':

    # 接收任务重规划参数，进行任务重规划
    rospy.init_node('re_plan_listener', annoymous=True)
    rospy.Subscriber('re_plan', String, callback)
    while message == '':
        continue
    re_plan_message = eval(message)
