import math

def solution(m, musicinfos):
    answer = [0, '(None)']
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    
    for info in musicinfos:
        start, end, title, music = info.split(',')
        hour, minute = map(int, start.split(':'))
        start = hour * 60 + minute
        
        hour, minute = map(int, end.split(':'))
        end = hour * 60 + minute
        minute = end - start
        
        music = music.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        music *= math.ceil(minute/len(music))
        total_music = music[:minute]
        
        if m in ''.join(total_music) and answer[0] < minute:
            answer[0] = minute
            answer[1] = title
    
    return answer[1]