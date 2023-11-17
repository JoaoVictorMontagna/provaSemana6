from flask import Flask, request, jsonify
app = Flask(__name__)

class CDB:
    def __init__(self, juros, valor_inicial, tempo, valor_final):
        self.juros = juros
        self.valor_inicial = valor_inicial
        self.tempo = tempo
        self.valor_final = valor_final

    def retornar_valor_projetado(self, valor_inicial, tempo):
        juros = float(self.juros)
        valor_final = valor_inicial * (1 + juros) ** tempo
        self.valor_final = valor_final

    def formatar_em_reais(self):
        valor_formatado = "R$ {:.2f}".format(self.valor_final)
        return valor_formatado

@app.route('/calcular_cdb', methods=['GET'])
def calcular_cdb():
    juros = request.args.get('juros', default=0.10, type=float)
    valor_inicial = request.args.get('valor_inicial', default=1000, type=float)
    tempo = request.args.get('tempo', default=2, type=int)

    investimento = CDB(juros, valor_inicial, tempo, 0)
    investimento.retornar_valor_projetado(valor_inicial, tempo)
    valor_formatado = investimento.formatar_em_reais()

    return jsonify({"Valor Esperado": valor_formatado})

if __name__ == '__main__':
    app.run(debug=True)
