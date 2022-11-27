import pandas as pd


# def extactTeamfightDataframe(teamfight_player_df:pd.DataFrame, match_id):
def extactTeamfightDataframe(select_match:pd.DataFrame):
    feature_list = ['delta_gold', 'delta_xp']
    sum_data = {}
    for i in feature_list:
        sum_data.update({'radiant_total_'+str(i):[],
                            'dire_total_'+str(i):[]})

    # select_match = teamfight_player_df.loc[teamfight_player_df['match_id']==match_id]
    fight_num = int((select_match.shape[0])/10)
    for j in range(fight_num):
        one_teamfight = select_match.iloc[(10*j):(10*(j+1)),:]
        radiant = one_teamfight.loc[one_teamfight['player_slot']<=4]
        dire = one_teamfight.loc[one_teamfight['player_slot']>4]
        for k in feature_list:
            sum_data['radiant_total_'+str(k)].append(radiant[k].sum())
            sum_data['dire_total_'+str(k)].append(dire[k].sum())
    return sum_data

def extactStatDatafram(select_match:pd.DataFrame):
    cols = ['gold_spent', 'gold_per_min', 'xp_per_min', 'kills', 'deaths', 
            'assists', 'denies', 'last_hits', 'stuns', 'hero_damage', 'hero_healing', 
            'tower_damage', 'level', 'leaver_status']
    sum_data = {}
    for j in cols:
        sum_data.update({'radiant_total_'+str(j):[],
                        'dire_total_'+str(j):[]})
    radiant = select_match.loc[select_match['player_slot']<=4]
    dire = select_match.loc[select_match['player_slot']>4]
    for j in cols:
        sum_data['radiant_total_'+str(j)].append(radiant[j].sum())
        sum_data['dire_total_'+str(j)].append(dire[j].sum())
    return sum_data
