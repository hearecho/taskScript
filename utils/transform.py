import json


def transformJson(file):
    """
    文件json转换为数据结构
    :param file: 转换文件路径
    :return: 转换完成的数据结构
    """
    with open(file, 'r', encoding='utf-8') as f:
        load_dict = json.load(f)
    return load_dict



if __name__ == '__main__':
    str = "{\"aid\":499909330,\"attribute\":16512,\"cid\":245746165,\"copyright\":1,\"ctime\":1602700342,\"desc\":\"\",\"dimension\":{\"height\":1080,\"rotate\":0,\"width\":1920},\"duration\":966,\"dynamic\":\"\",\"jump_url\":\"bilibili:\\/\\/video\\/499909330\\/?page=1&player_preload=null&player_width=1920&player_height=1080&player_rotate=0\",\"mission_id\":14723,\"owner\":{\"face\":\"https:\\/\\/i0.hdslb.com\\/bfs\\/face\\/6426336744dd49a744eca32855808073988bd2ce.jpg\",\"mid\":1935882,\"name\":\"指法芬芳张大仙\"},\"pic\":\"https:\\/\\/i1.hdslb.com\\/bfs\\/archive\\/f7be46eb50af91103c5bac5fc84b7559e0946363.jpg\",\"player_info\":null,\"pubdate\":1602700342,\"rights\":{\"autoplay\":1,\"bp\":0,\"download\":0,\"elec\":0,\"hd5\":0,\"is_cooperation\":0,\"movie\":0,\"no_background\":0,\"no_reprint\":1,\"pay\":0,\"ugc_pay\":0,\"ugc_pay_preview\":0},\"share_subtitle\":\"已观看12.0万次\",\"stat\":{\"aid\":499909330,\"coin\":697,\"danmaku\":1013,\"dislike\":0,\"favorite\":309,\"his_rank\":0,\"like\":10280,\"now_rank\":0,\"reply\":421,\"share\":175,\"view\":127055},\"state\":0,\"tid\":171,\"title\":\"王者荣耀大仙，用阿轲上王者，这乱杀的感觉不美妙吗\",\"tname\":\"电子竞技\",\"videos\":1}"
    print(json.loads(str))
