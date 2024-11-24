import requests


# url = "https://suo.yt/0PKQ4Yf"
url = ("https://sub.xeton.dev/sub?target=clash&new_name=true&url="
       "https://github.com/mai19950/free_site/raw/refs/heads/main/v2ray/base64|"
       "https://raw.githubusercontent.com/ripaojiedian/freenode/main/sub|"
       "https://trojan.fxxk.dedyn.io/auto"
       "&insert=false"
       "&config=https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online_Full_AdblockPlus.ini")

headers = {
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

def main():
  try:
    with requests.get(url, timeout=10, headers=headers) as res:
      if res.status_code < 300:
        with open('clash.yaml', mode="w+", encoding="utf-8") as f:
          f.write(res.text)
          print("节点保存成功")
      else:
        print("链接请求错误：", res.status_code)
  except Exception as e:
    print(e.args)
    main()


if __name__ == '__main__':
  main()