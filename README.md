
# 根据编号创建目录
convert_jav创建编号目录，把当前文件的视频移动进去，配合JAVMovieScraper使用
./convert_jav.py ~/nfs/hv/julia/


# 根据整轨文件名，批量创建目录, 层级最高2级
python3 ./cue2dir.py .

# 从上面建好的目录里，读取整轨，批量分割ape、flac、wav整轨为分轨, 层级最高2级
python3 ./toflac.py .


