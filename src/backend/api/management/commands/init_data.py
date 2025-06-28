import csv
from django.core.management.base import BaseCommand
from api.models import Categoria, Cargo, Departamento, Servidor, Vinculo
from django.utils import timezone
from pathlib import Path

class Command(BaseCommand):
    help = "Popula o banco de dados com dados iniciais fixos."

    def handle(self, *args, **kwargs):
        # self.stdout.write("Limpando dados antigos...")
        # Vinculo.objects.all().delete()
        # Servidor.objects.filter(is_superuser=False).delete()
        # Departamento.objects.all().delete()
        # Cargo.objects.all().delete()
        # Categoria.objects.all().delete()

        self.stdout.write("Criando Categorias...")
        categorias = [
            Categoria(nome_categoria="Docente"),
            Categoria(nome_categoria="Técnico Administrativo"),
        ]
        Categoria.objects.bulk_create(categorias)
        categorias_map = {cat.nome_categoria: cat for cat in Categoria.objects.all()}

        self.stdout.write("Criando Cargos...")
        cargos = [
            Cargo(nome_cargo="PROFESSOR DO MAGISTERIO SUPERIOR", categoria=categorias_map["Docente"]),
            Cargo(nome_cargo="ASSISTENTE EM ADMINISTRACAO", categoria=categorias_map["Técnico Administrativo"]),
            Cargo(nome_cargo="ASSISTENTE SOCIAL", categoria=categorias_map["Técnico Administrativo"]),
            Cargo(nome_cargo="TECNICO EM SEGURANCA DO TRABALHO", categoria=categorias_map["Técnico Administrativo"]),
            Cargo(nome_cargo="TRADUTOR INTERPRETE DE LINGUAGEM SINAIS", categoria=categorias_map["Técnico Administrativo"]),
            Cargo(nome_cargo="AUXILIAR EM ADMINISTRACAO", categoria=categorias_map["Técnico Administrativo"]),
            Cargo(nome_cargo="ENGENHEIRO-AREA", categoria=categorias_map["Técnico Administrativo"]),
            Cargo(nome_cargo="TECNICO DE TECNOLOGIA DA INFORMACAO", categoria=categorias_map["Técnico Administrativo"]),
            Cargo(nome_cargo="TECNICO EM ASSUNTOS EDUCACIONAIS", categoria=categorias_map["Técnico Administrativo"]),
            Cargo(nome_cargo="ADMINISTRADOR", categoria=categorias_map["Técnico Administrativo"]),
            Cargo(nome_cargo="BIBLIOTECARIO-DOCUMENTALISTA", categoria=categorias_map["Técnico Administrativo"]),
            Cargo(nome_cargo="TECNICO EM CONTABILIDADE", categoria=categorias_map["Técnico Administrativo"]),
            Cargo(nome_cargo="HISTORIADOR", categoria=categorias_map["Técnico Administrativo"]),
            Cargo(nome_cargo="PSICOLOGO-AREA", categoria=categorias_map["Técnico Administrativo"]),
            Cargo(nome_cargo="VIGILANTE", categoria=categorias_map["Técnico Administrativo"]),
        ]
        Cargo.objects.bulk_create(cargos)
        cargos_map = {cargo.nome_cargo: cargo for cargo in Cargo.objects.all()}

        self.stdout.write("Criando Departamentos...")
        departamentos = [
            Departamento(nome_depto="CERES - DEPARTAMENTO DE GEOGRAFIA", sigla_depto="DGC", latitude=-6.2, longitude=-37.1),
            Departamento(nome_depto="CERES - DEPARTAMENTO DE HISTÓRIA", sigla_depto="DHC", latitude=-6.5, longitude=-37.0),
            Departamento(nome_depto="CERES - DEPTO CIÊNCIAS EXATAS E APLICADAS", sigla_depto="DCEA", latitude=-6.2, longitude=-37.1),
            Departamento(nome_depto="CERES - DEPTO DE EDUCAÇÃO", sigla_depto="DEDUC", latitude=-6.2, longitude=-37.1),
            Departamento(nome_depto="ADMINISTRAÇÃO DO CERES - CAICÓ", sigla_depto="ADM-CAICO", latitude=-6.5, longitude=-37.5),
            Departamento(nome_depto="DEPARTAMENTO DE DIREITO - CERES", sigla_depto="DIR", latitude=-6.7, longitude=-37.8),
            Departamento(nome_depto="DEPARTAMENTO DE COMPUTAÇÃO E TECNOLOGIA", sigla_depto="DCT", latitude=-6.3, longitude=-37.9),
            Departamento(nome_depto="ASSESSORIA ADMINISTRATIVA DO CERES", sigla_depto="ASS-ADM", latitude=-6.5, longitude=-37.5),
            Departamento(nome_depto="CENTRO DE ENSINO SUPERIOR DO SERIDÓ", sigla_depto="CERES", latitude=-6.5, longitude=-37.5),
        ]
        Departamento.objects.bulk_create(departamentos)
        departamentos_map = {depto.nome_depto: depto for depto in Departamento.objects.all()}

        # 4. Dados dos servidores que seriam lidos do CSV
        servidores_data = [
            {'siape': '3289864', 'nome': 'ABNER MONTEIRO NUNES CORDEIRO', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE GEOGRAFIA', 'username': 'abner.cordeiro'},
            {'siape': '1668850', 'nome': 'ABRAHAO SANDERSON NUNES FERNANDES DA SILVA', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE HISTÓRIA', 'username': 'abrahao.silva'},
            {'siape': '350425', 'nome': 'ADRIANO MEDEIROS DE ARAUJO', 'cargo': 'ASSISTENTE EM ADMINISTRACAO', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'ADMINISTRAÇÃO DO CERES - CAICÓ', 'username': 'adriano.araujo'},
            {'siape': '2492701', 'nome': 'ADRIANO THIAGO LOPES BERNARDINO', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPTO CIÊNCIAS EXATAS E APLICADAS', 'username': 'adriano.bernardino'},
            {'siape': '2371256', 'nome': 'AIRAN DOS SANTOS BORGES DE OLIVEIRA', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE HISTÓRIA', 'username': 'airan.oliveira'},
            {'siape': '2321190', 'nome': 'ALEX DE MOURA BATISTA', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPTO CIÊNCIAS EXATAS E APLICADAS', 'username': 'alex.batista'},
            {'siape': '350481', 'nome': 'ALEX SANDRO MACEDO DE OLIVEIRA', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPTO CIÊNCIAS EXATAS E APLICADAS', 'username': 'alex.oliveira'},
            {'siape': '1337018', 'nome': 'ALISSA MARIANE GARCIA GRYMUZA', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPTO CIÊNCIAS EXATAS E APLICADAS', 'username': 'alissa.grymuza'},
            {'siape': '12746', 'nome': 'ALMIR MIRANDA FERREIRA', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'DEPARTAMENTO DE COMPUTAÇÃO E TECNOLOGIA', 'username': 'almir.ferreira'},
            {'siape': '2923129', 'nome': 'AMANDA KELLY BELO DA SILVA', 'cargo': 'ASSISTENTE SOCIAL', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'ADMINISTRAÇÃO DO CERES - CAICÓ', 'username': 'amanda.silva'},
            {'siape': '2784359', 'nome': 'ANA MONICA MEDEIROS FERREIRA', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'DEPARTAMENTO DE DIREITO - CERES', 'username': 'ana.ferreira'},
            {'siape': '1700539', 'nome': 'ANDRE MELO GOMES PEREIRA', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': '20 horas semanais', 'unidade': 'DEPARTAMENTO DE DIREITO - CERES', 'username': 'andre.pereira'},
            {'siape': '3214358', 'nome': 'ANE LUISE SILVA MECENAS SANTOS', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE HISTÓRIA', 'username': 'ane.santos'},
            {'siape': '3325346', 'nome': 'ANNA CLAUDIA DOS SANTOS NOBRE', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'DEPARTAMENTO DE COMPUTAÇÃO E TECNOLOGIA', 'username': 'anna.nobre'},
            {'siape': '3103247', 'nome': 'ANTONIO CARLOS ZEFERINO', 'cargo': 'TECNICO EM SEGURANCA DO TRABALHO', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'ADMINISTRAÇÃO DO CERES - CAICÓ', 'username': 'antonio.zeferino'},
            {'siape': '1040569', 'nome': 'ANTONIO JOSE DE OLIVEIRA', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE HISTÓRIA', 'username': 'antonio.oliveira'},
            {'siape': '3342435', 'nome': 'ANTONIO RODRIGUES XIMENES NETO', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE GEOGRAFIA', 'username': 'antonio.neto'},
            {'siape': '3103532', 'nome': 'ANTONIO SEBASTIAO DE LIMA', 'cargo': 'ASSISTENTE EM ADMINISTRACAO', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'ADMINISTRAÇÃO DO CERES - CAICÓ', 'username': 'antonio.lima'},
            {'siape': '2669476', 'nome': 'ARTHUR EMANOEL CASSIO DA SILVA E SOUZA', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'DEPARTAMENTO DE COMPUTAÇÃO E TECNOLOGIA', 'username': 'arthur.souza'},
            {'siape': '2131680', 'nome': 'CAIO ALEXANDRE ALENCAR DE MEDEIROS', 'cargo': 'AUXILIAR EM ADMINISTRACAO', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'ASSESSORIA ADMINISTRATIVA DO CERES', 'username': 'caio.medeiros'},
            {'siape': '2348083', 'nome': 'CARLOS FRANCISCO DO NASCIMENTO', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'DEPARTAMENTO DE DIREITO - CERES', 'username': 'carlos.nascimento'},
            {'siape': '2092005', 'nome': 'CLAUDIANE DOS SANTOS VASCONCELOS', 'cargo': 'TRADUTOR INTERPRETE DE LINGUAGEM SINAIS', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'ADMINISTRAÇÃO DO CERES - CAICÓ', 'username': 'claudiane.vasconcelos'},
            {'siape': '1997952', 'nome': 'DAVI DO VALE LOPES', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE GEOGRAFIA', 'username': 'davi.lopes'},
            {'siape': '3549987', 'nome': 'DESIO RAMIREZ DA ROCHA SILVA', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPTO CIÊNCIAS EXATAS E APLICADAS', 'username': 'desio.silva'},
            {'siape': '1804177', 'nome': 'DIEGO SALOMAO CANDIDO DE OLIVEIRA SALVADOR', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CENTRO DE ENSINO SUPERIOR DO SERIDÓ', 'username': 'diego.salvador'},
            {'siape': '1698154', 'nome': 'DIMITRE BRAGA SOARES DE CARVALHO', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'DEPARTAMENTO DE DIREITO - CERES', 'username': 'dimitre.carvalho'},
            {'siape': '348187', 'nome': 'EDNALDO AMERICO DE SOUZA', 'cargo': 'AUXILIAR EM ADMINISTRACAO', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'ADMINISTRAÇÃO DO CERES - CAICÓ', 'username': 'ednaldo.souza'},
            {'siape': '349959', 'nome': 'ELISIO PEREIRA DE ARAUJO JUNIOR', 'cargo': 'ENGENHEIRO-AREA', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'ADMINISTRAÇÃO DO CERES - CAICÓ', 'username': 'elisio.junior'},
            {'siape': '1244548', 'nome': 'EVANDRO DOS SANTOS', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE HISTÓRIA', 'username': 'evandro.santos'},
            {'siape': '1759940', 'nome': 'FABIO MAFRA BORGES', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE HISTÓRIA', 'username': 'fabio.borges'},
            {'siape': '1543250', 'nome': 'FABRICIO VALE DE AZEVEDO GUERRA', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'DEPARTAMENTO DE COMPUTAÇÃO E TECNOLOGIA', 'username': 'fabricio.guerra'},
            {'siape': '3655205', 'nome': 'FILLIPE AZEVEDO RODRIGUES', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'DEPARTAMENTO DE DIREITO - CERES', 'username': 'fillipe.rodrigues'},
            {'siape': '1687186', 'nome': 'FLAVIUS DA LUZ E GORGONIO', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'DEPARTAMENTO DE COMPUTAÇÃO E TECNOLOGIA', 'username': 'flavius.gorgonio'},
            {'siape': '1060541', 'nome': 'FRANCIMAR CARLOS DE MACEDO', 'cargo': 'TECNICO DE TECNOLOGIA DA INFORMACAO', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'ADMINISTRAÇÃO DO CERES - CAICÓ', 'username': 'francimar.macedo'},
            {'siape': '2334852', 'nome': 'FRANCIONE DA COSTA PEREIRA MEDEIROS', 'cargo': 'ASSISTENTE EM ADMINISTRACAO', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'ADMINISTRAÇÃO DO CERES - CAICÓ', 'username': 'francione.medeiros'},
            {'siape': '1757532', 'nome': 'FRANCISCO ANDERSON FREIRE PEREIRA', 'cargo': 'TECNICO DE TECNOLOGIA DA INFORMACAO', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'DEPARTAMENTO DE COMPUTAÇÃO E TECNOLOGIA', 'username': 'francisco.pereira'},
            {'siape': '277471', 'nome': 'FRANCISCO DAS CHAGAS MEDEIROS', 'cargo': 'AUXILIAR EM ADMINISTRACAO', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'ADMINISTRAÇÃO DO CERES - CAICÓ', 'username': 'francisco.medeiros'},
            {'siape': '2364748', 'nome': 'FRANCISCO MARCIO BARBOZA', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'DEPARTAMENTO DE COMPUTAÇÃO E TECNOLOGIA', 'username': 'francisco.barboza'},
            {'siape': '1759011', 'nome': 'FREUDSON DANTAS DE LIMA', 'cargo': 'ASSISTENTE EM ADMINISTRACAO', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'DEPARTAMENTO DE DIREITO - CERES', 'username': 'freudson.lima'},
            {'siape': '1804195', 'nome': 'GLEYDSON PINHEIRO ALBANO', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE GEOGRAFIA', 'username': 'gleydson.albano'},
            {'siape': '2432663', 'nome': 'HELDER ALEXANDRE MEDEIROS DE MACEDO', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE HISTÓRIA', 'username': 'helder.macedo'},
            {'siape': '1115783', 'nome': 'HERCIANE ARAUJO DE MELO', 'cargo': 'ASSISTENTE EM ADMINISTRACAO', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'CERES - DEPTO CIÊNCIAS EXATAS E APLICadas', 'username': 'herciane.melo'},
            {'siape': '1196714', 'nome': 'HUMBERTO RABELO', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'DEPARTAMENTO DE COMPUTAÇÃO E TECNOLOGIA', 'username': 'humberto.rabelo'},
            {'siape': '4891437', 'nome': 'IAPONY RODRIGUES GALVAO', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE GEOGRAFIA', 'username': 'iapony.galvao'},
            {'siape': '1747065', 'nome': 'IGOR FARIAS DE MEDEIROS', 'cargo': 'ASSISTENTE EM ADMINISTRACAO', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'ADMINISTRAÇÃO DO CERES - CAICÓ', 'username': 'igor.medeiros'},
            {'siape': '3159743', 'nome': 'IGOR RICARDO DE ALMEIDA CAVALCANTI', 'cargo': 'ADMINISTRADOR', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'ADMINISTRAÇÃO DO CERES - CAICÓ', 'username': 'igor.cavalcanti'},
            {'siape': '2329277', 'nome': 'JAILMA MARIA DE LIMA', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE HISTÓRIA', 'username': 'jailma.lima'},
            {'siape': '1332005', 'nome': 'JARLES TARSSO GOMES SANTOS', 'cargo': 'TECNICO EM ASSUNTOS EDUCACIONAIS', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'CENTRO DE ENSINO SUPERIOR DO SERIDÓ', 'username': 'jarles.santos'},
            {'siape': '3284957', 'nome': 'JEAN AUGUSTO HENRIQUE', 'cargo': 'ASSISTENTE EM ADMINISTRACAO', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'ADMINISTRAÇÃO DO CERES - CAICÓ', 'username': 'jean.henrique'},
            {'siape': '1804946', 'nome': 'JOAO BATISTA BORGES NETO', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'DEPARTAMENTO DE COMPUTAÇÃO E TECNOLOGIA', 'username': 'joao.neto'},
            {'siape': '350072', 'nome': 'JOAO INACIO SOARES', 'cargo': 'ASSISTENTE EM ADMINISTRACAO', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'ADMINISTRAÇÃO DO CERES - CAICÓ', 'username': 'joao.soares'},
            {'siape': '1450055', 'nome': 'JOAO MANOEL DE VASCONCELOS FILHO', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE GEOGRAFIA', 'username': 'joao.filho'},
            {'siape': '1804888', 'nome': 'JOAO PAULO DE SOUZA MEDEIROS', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'DEPARTAMENTO DE COMPUTAÇÃO E TECNOLOGIA', 'username': 'joao.medeiros'},
            {'siape': '1221431', 'nome': 'JOAO QUINTINO DE MEDEIROS FILHO', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE HISTÓRIA', 'username': 'joao.quintino'},
            {'siape': '1818226', 'nome': 'JOAO SANTIAGO REIS', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE GEOGRAFIA', 'username': 'joao.reis'},
            {'siape': '1414328', 'nome': 'JOEL CARLOS DE SOUZA ANDRADE', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE HISTÓRIA', 'username': 'joel.andrade'},
            {'siape': '3360412', 'nome': 'JORGE HENRIQUE DANTAS SILVA', 'cargo': 'ASSISTENTE EM ADMINISTRACAO', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'ADMINISTRAÇÃO DO CERES - CAICÓ', 'username': 'jorge.silva'},
            {'siape': '1103031', 'nome': 'JOSE BRAGA FILHO', 'cargo': 'VIGILANTE', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'ADMINISTRAÇÃO DO CERES - CAICÓ', 'username': 'jose.filho'},
            {'siape': '346683', 'nome': 'JOSE MEDEIROS FERREIRA', 'cargo': 'ADMINISTRADOR', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'ADMINISTRAÇÃO DO CERES - CAICÓ', 'username': 'jose.ferreira'},
            {'siape': '1112649', 'nome': 'JOSE YURE GOMES DOS SANTOS', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE GEOGRAFIA', 'username': 'jose.santos'},
            {'siape': '2914858', 'nome': 'JUCIENE BATISTA FELIX ANDRADE', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE HISTÓRIA', 'username': 'juciene.andrade'},
            {'siape': '1869739', 'nome': 'JUSSIER DO NASCIMENTO SOUZA', 'cargo': 'ASSISTENTE EM ADMINISTRACAO', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'CERES - DEPARTAMENTO DE HISTÓRIA', 'username': 'jussier.souza'},
            {'siape': '2720574', 'nome': 'KARLIANE MEDEIROS OVIDIO VALE', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'DEPARTAMENTO DE COMPUTAÇÃO E TECNOLOGIA', 'username': 'karliane.vale'},
            {'siape': '2410462', 'nome': 'KATTARINE DE MEDEIROS LUCENA', 'cargo': 'ASSISTENTE EM ADMINISTRACAO', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'DEPARTAMENTO DE COMPUTAÇÃO E TECNOLOGIA', 'username': 'kattarine.lucena'},
            {'siape': '1333956', 'nome': 'LARISSA JACHETA RIBERTI', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE HISTÓRIA', 'username': 'larissa.riberti'},
            {'siape': '3214278', 'nome': 'LEANDRO VIEIRA CAVALCANTE', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE GEOGRAFIA', 'username': 'leandro.cavalcante'},
            {'siape': '1718551', 'nome': 'LOURIVAL ANDRADE JUNIOR', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE HISTÓRIA', 'username': 'lourival.junior'},
            {'siape': '1291581', 'nome': 'LUCAS ALLAN DINIZ SCHWARZ', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPTO CIÊNCIAS EXATAS E APLICADAS', 'username': 'lucas.schwarz'},
            {'siape': '349709', 'nome': 'LUIS GONZAGA VIEIRA FILHO', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPTO CIÊNCIAS EXATAS E APLICADAS', 'username': 'luis.filho'},
            {'siape': '1804944', 'nome': 'LUIZ PAULO DE ASSIS BARBOSA', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'DEPARTAMENTO DE COMPUTAÇÃO E TECNOLOGIA', 'username': 'luiz.barbosa'},
            {'siape': '2179045', 'nome': 'LUZIANA MARIA NUNES DE QUEIROZ', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPTO CIÊNCIAS EXATAS E APLICADAS', 'username': 'luziana.queiroz'},
            {'siape': '2506087', 'nome': 'MARCO TULIO MENDONCA DINIZ', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE GEOGRAFIA', 'username': 'marco.diniz'},
            {'siape': '1757294', 'nome': 'MARCUS VINICIUS PEREIRA JUNIOR', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': '20 horas semanais', 'unidade': 'DEPARTAMENTO DE DIREITO - CERES', 'username': 'marcus.junior'},
            {'siape': '2378532', 'nome': 'MARIA DO SOCORRO VALENTIM', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPTO CIÊNCIAS EXATAS E APLICADAS', 'username': 'maria.valentim'},
            {'siape': '2204644', 'nome': 'MARIA JUCIMEIRE DOS SANTOS', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPTO CIÊNCIAS EXATAS E APLICADAS', 'username': 'maria.santos'},
            {'siape': '2009206', 'nome': 'MARIA MARONI LOPES', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPTO CIÊNCIAS EXATAS E APLICADAS', 'username': 'maria.lopes'},
            {'siape': '3085801', 'nome': 'MARTINA LUCIANA SOUZA BRIZOLARA', 'cargo': 'BIBLIOTECARIO-DOCUMENTALISTA', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'ADMINISTRAÇÃO DO CERES - CAICÓ', 'username': 'martina.brizolara'},
            {'siape': '1968846', 'nome': 'MATHEUS SILVA DANTAS DE QUEIROZ SOUZA', 'cargo': 'ASSISTENTE EM ADMINISTRACAO', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'CERES - DEPARTAMENTO DE GEOGRAFIA', 'username': 'matheus.souza'},
            {'siape': '3277226', 'nome': 'MAYARA BEZERRA BARBOSA', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPTO CIÊNCIAS EXATAS E APLICADAS', 'username': 'mayara.barbosa'},
            {'siape': '3431805', 'nome': 'MAYCON JEBSON DANTAS', 'cargo': 'TECNICO DE TECNOLOGIA DA INFORMACAO', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'CENTRO DE ENSINO SUPERIOR DO SERIDÓ', 'username': 'maycon.dantas'},
            {'siape': '3358339', 'nome': 'MILENA JEIMISSA DE LIMA SOUSA', 'cargo': 'ASSISTente EM ADMINISTRACAO', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'ADMINISTRAÇÃO DO CERES - CAICÓ', 'username': 'milena.sousa'},
            {'siape': '1831652', 'nome': 'NAINA LEITE DE LIMA', 'cargo': 'ASSISTENTE EM ADMINISTRACAO', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'ADMINISTRAÇÃO DO CERES - CAICÓ', 'username': 'naina.lima'},
            {'siape': '3122950', 'nome': 'NAJARA OLIVEIRA BERNARDO', 'cargo': 'ASSISTENTE EM ADMINISTRACAO', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'ADMINISTRAÇÃO DO CERES - CAICÓ', 'username': 'najara.bernardo'},
            {'siape': '1448916', 'nome': 'ORIONE DANTAS DE MEDEIROS', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'DEPARTAMENTO DE DIREITO - CERES', 'username': 'orione.medeiros'},
            {'siape': '1934542', 'nome': 'PAULA REJANE FERNANDES', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE HISTÓRIA', 'username': 'paula.fernandes'},
            {'siape': '2023386', 'nome': 'PHILIPPE MANOEL DE BARROS CARVALHO CANUTO', 'cargo': 'AUXILIAR EM ADMINISTRACAO', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'ADMINISTRAÇÃO DO CERES - CAICÓ', 'username': 'philippe.canuto'},
            {'siape': '3159602', 'nome': 'RAFAEL VIEIRA DE AZEVEDO', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'DEPARTAMENTO DE DIREITO - CERES', 'username': 'rafael.azevedo'},
            {'siape': '1759367', 'nome': 'REBECCA LUNA LUCENA', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE GEOGRAFIA', 'username': 'rebecca.lucena'},
            {'siape': '350720', 'nome': 'REILDA DE MEDEIROS MAIA LIMA', 'cargo': 'ASSISTENTE EM ADMINISTRACAO', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'ADMINISTRAÇÃO DO CERES - CAICÓ', 'username': 'reilda.lima'},
            {'siape': '1357743', 'nome': 'ROBERTO SILVA DA PENHA', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPTO CIÊNCIAS EXATAS E APLICADAS', 'username': 'roberto.penha'},
            {'siape': '1869367', 'nome': 'RODRIGO COSTA FERREIRA', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': '20 horas semanais', 'unidade': 'DEPARTAMENTO DE DIREITO - CERES', 'username': 'rodrigo.ferreira'},
            {'siape': '1516520', 'nome': 'ROGERIO DE ARAUJO LIMA', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CENTRO DE ENSINO SUPERIOR DO SERIDÓ', 'username': 'rogerio.lima'},
            {'siape': '396683', 'nome': 'SANDRA KELLY DE ARAUJO', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE GEOGRAFIA', 'username': 'sandra.araujo'},
            {'siape': '1726169', 'nome': 'SARA FERNANDES FLOR DE SOUZA', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE GEOGRAFIA', 'username': 'sara.souza'},
            {'siape': '3084976', 'nome': 'SAUL LINCOLN BEZERRA DE ARAUJO', 'cargo': 'TECNICO EM CONTABILIDADE', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'ADMINISTRAÇÃO DO CERES - CAICÓ', 'username': 'saul.araujo'},
            {'siape': '1574643', 'nome': 'SIMONE DA SILVA COSTA', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE HISTÓRIA', 'username': 'simone.costa'},
            {'siape': '2610304', 'nome': 'SOCRATES DANTAS LOPES', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPTO CIÊNCIAS EXATAS E APLICADAS', 'username': 'socrates.lopes'},
            {'siape': '1721652', 'nome': 'TACIANO DE MORAIS SILVA', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'DEPARTAMENTO DE COMPUTAÇÃO E TECNOLOGIA', 'username': 'taciano.silva'},
            {'siape': '1919171', 'nome': 'THALES LORDAO DIAS', 'cargo': 'ASSISTENTE EM ADMINISTRACAO', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'ADMINISTRAÇÃO DO CERES - CAICÓ', 'username': 'thales.dias'},
            {'siape': '1216653', 'nome': 'THIAGO ADRIANO MACHADO', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE GEOGRAFIA', 'username': 'thiago.machado'},
            {'siape': '2398884', 'nome': 'TIAGO TAVARES E SILVA', 'cargo': 'HISTORIADOR', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'ADMINISTRAÇÃO DO CERES - CAICÓ', 'username': 'tiago.silva'},
            {'siape': '1276740', 'nome': 'UBIRATHAN ROGERIO SOARES', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE HISTÓRIA', 'username': 'ubirathan.soares'},
            {'siape': '2527334', 'nome': 'VANESSA SPINOSA', 'cargo': 'PROFESSOR DO MAGISTERIO SUPERIOR', 'tipo_jornada_trabalho': 'Dedicação exclusiva', 'unidade': 'CERES - DEPARTAMENTO DE HISTÓRIA', 'username': 'vanessa.spinosa'},
            {'siape': '1152324', 'nome': 'YLGUEM DORIA COSTA', 'cargo': 'PSICOLOGO-AREA', 'tipo_jornada_trabalho': '40 horas semanais', 'unidade': 'ADMINISTRAÇÃO DO CERES - CAICÓ', 'username': 'ylguem.costa'},
        ]

        self.stdout.write("Criando Servidores...")
        servidores_para_criar = []
        for data in servidores_data:
            servidor = Servidor(
                username=data['username'],
                siape=data['siape'],
                nome_servidor=data['nome'],
                carga_horaria=data['tipo_jornada_trabalho']
            )
            servidor.set_password('123123123')
            servidores_para_criar.append(servidor)
        
        Servidor.objects.bulk_create(servidores_para_criar, ignore_conflicts=True)

        servidores_map = {s.username: s for s in Servidor.objects.all()}

        self.stdout.write("Criando Vínculos...")
        vinculos_para_criar = []
        for data in servidores_data:
            cargo = cargos_map.get(data['cargo'])
            departamento = departamentos_map.get(data['unidade'])
            servidor = servidores_map.get(data['username'])
            
            if not all([cargo, departamento, servidor]):
                self.stdout.write(self.style.WARNING(f"Não foi possível criar vínculo para {data['nome']}. Dados ausentes."))
                continue

            vinculo = Vinculo(
                servidor=servidor,
                cargo=cargo,
                departamento=departamento,
                data_inicio=timezone.now().date(),
                data_fim=None
            )
            vinculos_para_criar.append(vinculo)
            
        Vinculo.objects.bulk_create(vinculos_para_criar)

        self.stdout.write(self.style.SUCCESS("Banco de dados populado com sucesso!"))
