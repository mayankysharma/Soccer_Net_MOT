from SoccerNet.Downloader import SoccerNetDownloader
mySoccerNetDownloader = SoccerNetDownloader(LocalDirectory="/home/bowen/Code/soccer/data/")
mySoccerNetDownloader.downloadDataTask(task="tracking", split=["train", "test", "challenge"])