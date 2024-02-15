n, m = map(int, input().split())
nums = [0]*m

min_lens = set()
now = {}

for _ in range(n):
    buf = list(map(int, input().split()))
    for i in range(len(buf)):
        if buf[i] == 1:
            nums[i] += 1
            if nums[i] in now:
                now[nums[i]] += 1
                for key in now.keys():
                    if key < nums[i]:
                        now[key] += 1
                    elif key > nums[i]:
                        min_lens.add(min(key, now[key]))
            else:
                now[nums[i]] = 1
                vals = []
                for key in now.keys():
                    if key < nums[i]:
                        now[key] += 1
                    elif key > nums[i]:
                        vals.append(now[key])
                        min_lens.add(min(key, now[key]))
                if len(vals) > 0:
                    now[nums[i]] += max(vals)
            
            now = {key: el for key, el in now.items() if key <= nums[i]}

        else:
            nums[i] = 0
            for key in now.keys():
                min_lens.add(min(key, now[key]))
            now.clear()
    for key in now.keys():
        min_lens.add(min(key, now[key]))
    now.clear()
    
if len(min_lens) == 0: print(0)
else: print(max(min_lens))
            
        
    
