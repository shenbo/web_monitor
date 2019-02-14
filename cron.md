
## 显示已有任务
```crontab -l```

## 编辑任务
```crontab -e```

## 示例
```
# m h dom mon dow command
0 7-22 * * * python3 xx.py &

0 7 * * * python3 web_monitor/gold_price/gold_price.py &
1 7,12 * * * python3 web_monitor/gaoxiao_job/gaoxiao_job.py &
```