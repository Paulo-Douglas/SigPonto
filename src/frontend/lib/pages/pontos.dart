import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import '../utils/format_date.dart';
import '../styles/colors.dart';

// ignore: use_key_in_widget_constructors
class TelaRelatorio extends HookWidget {
  @override
  Widget build(BuildContext context) {
    final relatorios =
        ModalRoute.of(context)?.settings.arguments as List<dynamic>;

    return Scaffold(
      appBar: AppBar(title: Text("Relatórios")),
      body: relatorios.isEmpty
          ? Center(child: Text("Nenhum relatório disponível."))
          : ListView.separated(
              padding: EdgeInsets.all(16.0),
              itemCount: relatorios.length,
              separatorBuilder: (_, __) => Divider(),
              itemBuilder: (context, index) {
                final relatorio = relatorios[index];
                final dataHora = formatarData(relatorio["data_hora"]);
                final tipo = relatorio["tipo_ponto_display"];
                final servidor = relatorio["servidor_nome"];

                return ListTile(
                  leading: CircleAvatar(
                    backgroundColor: tipo == "Entrada"
                        ? GetColor.greeSuav.color
                        : GetColor.redLigth.color,
                    child: Icon(
                      tipo == "Entrada" ? Icons.login : Icons.logout,
                      color: tipo == "Entrada"
                          ? GetColor.greeLight.color
                          : GetColor.red.color,
                    ),
                  ),
                  title: Text(
                    servidor,
                    style: Theme.of(context).textTheme.titleMedium,
                  ),
                  subtitle: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(tipo, style: Theme.of(context).textTheme.bodySmall),
                      SizedBox(height: 4),
                      Text(
                        dataHora,
                        style: Theme.of(context).textTheme.bodySmall,
                      ),
                    ],
                  ),
                  isThreeLine: true,
                );
              },
            ),
    );
  }
}
