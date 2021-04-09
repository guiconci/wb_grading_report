import dash
from dash.dependencies import Input, Output
from dash_html_components.Div import Div
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np

app = dash.Dash(__name__)
server = app.server
#CREATE DF
df = pd.read_csv('https://raw.githubusercontent.com/guiconci/test_app/main/plan.csv')
df.set_index('id',inplace=True, drop=False)


df2 = pd.read_csv('https://raw.githubusercontent.com/guiconci/test_app/main/plan_2.csv')
df2.set_index('id',inplace=True, drop=False)


#CONSOLIDATE GRADING
#  SOME LEATHER CAN USE ONE OF TWO GRADES, SO WE ALWAYS CONSIDER THE 'BEST GRADE'
double_grade = {'B/BV':'B', 'C/CV':'C', 'B/C':'B', 'CV/D':'CV'}
grade_list = ['B', 'BV', 'C', 'CV', 'D']

# REPLACE IN DF AND DF2 THE DOUBLE GRADE ENTRIES BY THE 'BEST GRADE'    
for x in df.id:
    for key in double_grade:
        if key == df['Grade'][x]:
            df.loc[x,'Grade'] = double_grade.get(key)
    
for x in df2.id:
    for key in double_grade:
        if key == df2['Grade'][x]:
            df2.loc[x,'Grade'] = double_grade.get(key)

#FUNCTION TO GET SUM OF SIDESSS
#DF1 2.02
def sum_wb2(grading):
    sides = 0
    for g in df['id']:
        if df["Grade"][g] == grading and df["Substance"][g]<2.0:
            sides = sides + df["Sides"][g]
    return(sides)

#DF2 2.02
def sum_wb2_1(grading):
    sides = 0
    for g in df2['id']:
        if df2["Grade"][g] == grading and df2["Substance"][g]<2.0:
            sides = sides + df2["Sides"][g]
    return(sides)

#DF1 2.46
def sum_wb4(grading):
    sides = 0
    for g in df['id']:
        if df["Grade"][g] == grading and df["Substance"][g]>2.0:
            sides = sides + df["Sides"][g]
    return(sides)

#DF2 2.46
def sum_wb4_1(grading):
    sides = 0
    for g in df2['id']:
        if df2["Grade"][g] == grading and df2["Substance"][g]>2.0:
            sides = sides + df2["Sides"][g]
    return(sides)


#PREPARE DATA FOR APP LAYOUT DATA REQUIREMENT LIST OF DICTIONARIES CALL FUNCTION
dicts = []
for g in grade_list:
    d = {'sides': sum_wb2(g)}
    d['grade'] = g
    dicts.append(d)

dicts2 = []
for g in grade_list:
    d = {'sides': sum_wb2_1(g)}
    d['grade'] = g
    dicts2.append(d)

dicts3 = []
for g in grade_list:
    d = {'sides': sum_wb4(g)}
    d['grade'] = g
    dicts3.append(d)

dicts4 = []
for g in grade_list:
    d = {'sides': sum_wb4_1(g)}
    d['grade'] = g
    dicts4.append(d)

#SET DATE FOR DF 1 and 2
date1 = df['RT Date'][1]
date2 = df2['RT Date'][1]


#tst = df["Substance"][1]
#if tst < 2 and tst == 1.82:
#    print(tst, 'ok')
#else:
#    print(tst, 'no ok')
#print(sum_wb2('C'))

#for g in df2['id']:
#        if df2["Grade"][g] == 'C' and df2["Substance"][g]>2.0:
#            print(df['id'][g])

#print(2>2)


#DATA TABLES
#DIV WITH DATA TABLES INISIDE AND STYLE
# THCKNESS 20 = 2.02 mm AND 24 = 2.46    
thick_20 = html.Div(
            
            className='row',
            style = {'display' : 'inline-block'},
            children=[
                html.H1(id='Title2',children='2.02 mm',
                style={'text-align':'center','font': '20px Arial, sans-serif'}),

                html.Div(
                className='row',
                style = {'display' : 'flex'},
                children=[
                dash_table.DataTable(
                id='table-2.02-plan1',
                columns=[
                    {
                    'name': [date1,'Grade'],'id': 'grade',
                    'deletable': True,
                    'renamable': True
                    },
                    {
                    'name': [date1,'Sides'], 'id': 'sides',
                    'deletable': True,
                    'renamable': True
                    }
                    ],
                merge_duplicate_headers=True,
                
                data= dicts,
                #STYLE
                style_table={'border-right':'solid','border-right-width':'thin'}, 
                fill_width=False,                                
                editable=True,  
                style_as_list_view=True),
            dash_table.DataTable(
                    id='table-2.02-plan2',
                    columns=[
                        {
                        'name': [date2,'Grade'],'id': 'grade',
                        'deletable': True,
                        'renamable': True
                        },
                        {
                        'name': [date2,'Sides'], 'id': 'sides',
                        'deletable': True,
                        'renamable': True
                        }
                        ],
                    merge_duplicate_headers=True,
                    data= dicts2,
                    #STYLE
                    style_table={'border-right':'solid','border-right-width':'thin',
                                'border-left':'solid','border-left-width':'thin'},
                    fill_width=False,                                
                    editable=True,
                    style_as_list_view=True)]
                    )
                    ])
thick_24 = html.Div(
            
            className='row',
            style = {'display' : 'inline-block'},
            children=[
                html.H1(id='Title1',children='2.46 mm',
                style={'text-align':'center', 'font': '20px Arial, sans-serif'}),

                html.Div(
                className='row',
                style = {'display' : 'flex'},
                children=[
                dash_table.DataTable(
                    id='table-2.46-plan1',
                    columns=[
                        {
                        'name': [date1,'Grade'],'id': 'grade',
                        'deletable': True,
                        'renamable': True
                        },
                        {
                        'name': [date1,'Sides'], 'id': 'sides',
                        'deletable': True,
                        'renamable': True
                        }
                        ],
                    merge_duplicate_headers=True,
                    data= dicts,
                    #STYLE
                    style_table={'border-right':'solid','border-right-width':'thin',
                                'border-left':'solid','border-left-width':'thin'},
                    fill_width=False,                                
                    editable=True,
                    style_as_list_view=True),
            dash_table.DataTable(
                    id='table-2.46-plan2',
                    columns=[
                        {
                        'name': [date2,'Grade'],'id': 'grade',
                        'deletable': True,
                        'renamable': True
                        },
                        {
                        'name': [date2,'Sides'], 'id': 'sides',
                        'deletable': True,
                        'renamable': True
                        }
                        ],
                    merge_duplicate_headers=True,
                    data= dicts2,
                    #STYLE
                    style_table={'border-right':'solid','border-right-width':'thin',
                                'border-left':'solid','border-left-width':'thin'},
                    fill_width=False,                                
                    editable=True,
                    style_as_list_view=True)]
                    )
                    ])
title = html.Div(
            
            
            html.H1(id='Title0',children='WET BLUE NEEDED ACCORDING TO RETAN PLAN',
            style={'text-align':'center','font': '30px Arial, sans-serif'}, className='row'))

app.layout = html.Div(
            
            className='row',
            style = {'display' : 'inline'},
            children=[
        title,
        html.Div(style={'display':'flex','justify-content':'center'},
            children=[thick_20, thick_24])
        

        ])
        

# html.Div(style= {"border-right":'solid',"border-right-width":"2px", "border-right-color":"black"},
    
if __name__ == '__main__':
    app.run_server(debug=True)

