from urllib import response
from apiclient.discovery import build
import datetime
import pandas as pd
import sys
import os

argv = sys.argv
#####
YOUTUBE_API_KEY = argv[1]
RANK_NUM = 10
SEARCH_TITLE = 'ポケモン'
DAY_SPAN = 1
PATH_W = 'youtube_rank.md'
TIME＿DIFFERENCE = int(argv[2])
###########

def main():
    dt_now = datetime.datetime.now() + datetime.timedelta(hours=TIME_DIFFERENCE) 
    dt_now_after = dt_now - datetime.timedelta(days=DAY_SPAN)
    youtube = make_youtube_instance(YOUTUBE_API_KEY=YOUTUBE_API_KEY)
    response = search_youtube_keyword(
    youtube=youtube,
    part='snippet',
    q=SEARCH_TITLE,
    type='video',
    order='viewCount',
    maxResults=RANK_NUM,
    publishedAfter=dt_now_after.strftime('%Y-%m-%dT%H:%M:%SZ'),
    publishedBefore=None,
    regionCode='JP')
    df = make_dataframe(youtube=youtube,response=response)
    ###df.to_pickle('youtube_rank.pkl')
    ###df = pd.read_pickle('youtube_rank.pkl')
    
    with open(PATH_W, mode='w') as f:
        write_file(f,df, SEARCH_TITLE, dt_now, dt_now_after)

def make_youtube_instance(YOUTUBE_API_KEY):
    return build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def search_youtube_keyword(youtube,part,q,type,order,maxResults,publishedAfter,publishedBefore,regionCode):
    if publishedAfter == None and publishedBefore == None:
        return youtube.search().list(
        part=part,
        q=q,
        type=type,
        order=order,
        maxResults=maxResults,
        regionCode=regionCode
        ).execute()
    elif publishedAfter != None and publishedBefore != None:
        return youtube.search().list(
        part=part,
        q=q,
        type=type,
        order=order,
        maxResults=maxResults,
        publishedAfter=publishedAfter,
        publishedBefore=publishedBefore,
        regionCode=regionCode
        ).execute()
    elif publishedAfter == None and publishedBefore != None:
        return youtube.search().list(
        part=part,
        q=q,
        type=type,
        order=order,
        maxResults=maxResults,
        publishedBefore=publishedBefore,
        regionCode=regionCode
        ).execute()
    elif  publishedAfter != None and publishedBefore == None:
        return youtube.search().list(
        part=part,
        q=q,
        type=type,
        order=order,
        maxResults=maxResults,
        publishedAfter=publishedAfter,
        regionCode=regionCode
        ).execute()
    else:
        print('Error', file=sys.stderr)     
            
def make_dataframe(youtube,response): 
    df = pd.DataFrame(response['items'])
    df1 = pd.DataFrame(list(df['id']))['videoId']
    df2 = pd.DataFrame(list(df['snippet']))[['channelTitle','publishedAt','channelId','title']]
    df3 = pd.concat([df1,df2], axis = 1)
    df4 = pd.DataFrame(list(df3['videoId'].apply(lambda x : get_statistics(id=x,youtube=youtube))))
    df5 = pd.concat([df3,df4], axis = 1)
    links = ["http://www.youtube.com/watch?v="+x for x in  df5['videoId']]
    df5.insert(len(df5.columns), 'movie_URL', links)
    return(df5)

def get_statistics(id,youtube):
    statistics = youtube.videos().list(part = 'statistics', id = id).execute()['items'][0]['statistics']
    return statistics

def write_file(f,df, title, dt_now, dt_now_after):
    f.write('# '+title+' YouTube 再生回数 ランキング\n')

    f.write('---\n## 期間 : '+dt_now_after.strftime('%Y年%m月%d日%H時%M分%S秒')+' ~ '+dt_now.strftime('%Y年%m月%d日%H時%M分%S秒')+'\n')
    for i in range(len(df.index)):
        title = df.at[i,'title']
        f.write('* ['+'第'+str(i+1)+'位 : '+title+'](#第'+str(i+1)+'位)\n')

    for i in range(len(df.index)):
        movie_URL = df.at[i,'movie_URL']
        channelTitle = df.at[i,'channelTitle']
        title = df.at[i,'title']
        viewCount = df.at[i,'viewCount']
        publishedAt = df.at[i,'publishedAt']
        f.write('# 第'+str(i+1)+'位\n')
        f.write('- ['+ title +']'+'('+movie_URL+')'+'\n')
        f.write('   - チャンネル名 : '+channelTitle+'\n')
        f.write('       - 再生数 : '+viewCount+'回\n\n')
        f.write(html_youtube(df.at[i,'videoId'])+"\n")

def html_youtube(link,width=560,height=315):
    string = "<iframe width=\""+str(width)+"\" height=\""+str(height)+"\" src=\"https://www.youtube.com/embed/"+link+"\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>\n"
    return string




main()

