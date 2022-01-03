import time
import json
from loguru import logger
from service.constants import mensagens
import pandas as pd
import numpy as np

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class QuadraticEquation():

    def __init__(self):
        logger.debug(mensagens.INICIO_LOAD_CALCULADORA)
        self.load_model()

    def load_model(self):
        """"
        Carrega a calculadora a ser utilizada
        """

        logger.debug(mensagens.FIM_LOAD_CALCULADORA)

    def executar_rest(self, texts):
        response = {}

        logger.debug(mensagens.INICIO_CALCULO)
        start_time = time.time()

        response_predicts = self.calcular_equacao_quadratica(texts['textoMensagem'])

        logger.debug(mensagens.FIM_CALCULO)
        logger.debug(f"Fim de todas as predições em {time.time()-start_time}")

        df_response = pd.DataFrame(texts, columns=['textoMensagem'])
        df_response['predict'] = response_predicts

        df_response = df_response.drop(columns=['textoMensagem'])

        response = {
                     "listaClassificacoes": json.loads(df_response.to_json(
                                                                            orient='records', force_ascii=False))}

        return response

    def calcular_equacao_quadratica(self, texts):
        """
        Resolve a equacao de segundo grau escrita em texts
        """
        logger.debug('Iniciando o calculo...')

        response = []

        for text in texts:
            a, b, c = text.split()
            equacao =  a + "xˆ2 + " + b + "x + " + c
            a = float(a)
            b = float(b)
            c = float(c)
            delta = (b**2 - 4*a*c)
            x1 = (-b + delta**(1/2)) / (2*a)
            x2 = (-b - delta**(1/2)) / (2*a)
             
            response.append(equacao + " : " + "S = {" + str(x1) + ", " + str(x2) + "}")
            
        return response