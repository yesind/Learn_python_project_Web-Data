import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = "afjahsflhasdf4io25o740tygh958yg9e5hg5h89phgp5hp95qgp98w5hwpg5"


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'auto.db')

marks = ['AUDI', "BMW", "MERCEDES", "LAND_ROVER"]
models = ['A1', 'A2', 'A3', 'A4', 'A4_ALLROAD', 'A5', 'A6', 'A7', 'A8', 'ALLROAD', 
        'E_TRON', 'Q2', 'Q3', 'Q3_SPORTBACK', 'Q4', 'Q4_SPORTBACK', 'Q5', 
        'Q5_E_TRON', 'Q5_SPORTBACK', 'Q7', 'Q8', 'R8', 'RS3', 'RS4', 'RS5', 'RS6', 
        'RS7', 'RSQ3', 'RS_E_TRON_GT', 'RS_Q3_SPORTBACK', 'RS_Q8', 'S1', 'S2', 'S3', 
        'S4', 'S5', 'S6', 'S7', 'S8', 'SQ2', 'SQ5', 'SQ5_SPORTBACK', 'SQ7', 'SQ8', 'TT', 'TTS', 'TT_RS']

models_mercedes = ['AMG_GLC_COUPE', 'A_KLASSE', 'A_KLASSE_AMG', 'B_KLASSE', 'CLA_KLASSE', 'CLA_KLASSE_AMG', 
                'CLC_KLASSE', 'CLK_AMG_GTR', 'CLK_KLASSE', 'CLK_KLASSE_AMG', 'CLS_KLASSE', 'CLS_KLASSE_AMG', 
                'CL_KLASSE', 'CL_KLASSE_AMG', 'C_KLASSE', 'C_KLASSE_AMG', 'EQA', 'EQB', 'EQC', 'EQE', 
                'EQE_AMG', 'EQE_SUV', 'EQE_SUV_AMG', 'EQS', 'EQS_AMG', 'EQS_SUV', 'EQV', 'E_KLASSE', 
                'E_KLASSE_AMG', 'GLA_CLASS', 'GLA_CLASS_AMG', 'GLB_AMG', 'GLB_KLASSE', 'GLC_COUPE', 
                'GLC_KLASSE', 'GLC_KLASSE_AMG', 'GLE_KLASSE', 'GLE_KLASSE_AMG', 'GLE_KLASSE_COUPE', 
                'GLE_KLASSE_COUPE_AMG', 'GLK_KLASSE', 'GLS_KLASSE', 'GLS_KLASSE_AMG', 'GL_KLASSE', 
                'GL_KLASSE_AMG', 'G_KLASSE', 'G_KLASSE_AMG', 'MAYBACH_GLS', 'MAYBACH_G_650', 'SLC_KLASSE', 
                'SLC_KLASSE_AMG', 'SLK_KLASSE', 'SLK_KLASSE_AMG', 'SLR_KLASSE', 'SLS_AMG', 'SL_KLASSE', 
                'SL_KLASSE_AMG', 'S_CLASS_MAYBACH', 'T_KLASSE', 'VIANO', 'VITO', 'V_KLASSE']

models_bmw = ['2ER', '3ER', '4', '5ER', '6ER', '7ER', 'IX', 'IX1', 'IX3', 'M3', 'M4', 'M5', 'M6', 
            'M8', 'X1', 'X2', 'X3', 'X3_M', 'X4', 'X4_M', 'X5', 'X5_M', 'X6', 'X6_M', 'X7']

models_LR = ['DEFENDER', 'DISCOVERY', 'DISCOVERY_SPORT', 'EVOQUE', 'FREELANDER', 'RANGE_ROVER', 
            'RANGE_ROVER_SPORT', 'RANGE_ROVER_VELAR']

fuel = ['GASOLINE', 'DIESEL', 'ELECTRO']
gear_type = ['ALL_WHEEL_DRIVE',"FORWARD_CONTROL","REAR_DRIVE"]
owners_count_group = ["ONE", "LESS_THAN_TWO"]


