#coding=utf-8


if __name__=="__main__":
    path = "C:\Users\kaiw.CITRITE\Downloads\Fake-Followers\Fake Follower Network.csv"
    fake_user = set()
    with open(path,'r') as f:
        for line in f:
            fake_user.add(line.split(",")[0])
    # print fake_user
    f = open("./FakeFollower/username",'w')
    fake_user = sorted(fake_user)
    for user in fake_user:
        f.write(user+"\n")
    f.close()