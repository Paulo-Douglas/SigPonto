import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'dart:async';
import '../components/my_button.dart';
import '../service/service.dart';
import '../utils/format_date.dart';
import '../styles/colors.dart';

class TelaHome extends HookWidget {
  final double width;
  final double height;

  const TelaHome({super.key, required this.width, required this.height});

  @override
  Widget build(BuildContext context) {
    var ponto = useState([]);

    return Scaffold(
      appBar: AppBar(
        title: Text("SIGPONTO"),
        leading: IconButton(
          icon: Icon(Icons.logout),
          onPressed: () async {
            var logout = await SERVICE.logout(SERVICE.username, SERVICE.token);
            if (logout) Navigator.pop(context);
          },
        ),
      ),
      body: Container(
        width: double.infinity,
        decoration: BoxDecoration(
          color: Theme.of(context).colorScheme.onPrimary,
        ),
        child: Column(
          children: [
            Expanded(
              child: SizedBox(
                height: height * 0.5,
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  spacing: 50,
                  children: [
                    MyButton(
                      actionButton: "Visualizar minhas presenças",
                      onPressed: () async {
                        var relatorios = await SERVICE.pontosRelatorio(
                          SERVICE.token,
                        );
                        Navigator.pushNamed(
                          context,
                          '/pontos',
                          arguments: relatorios,
                        );
                      },
                      styleButton: "yellow",
                    ),
                    MyButton(
                      actionButton: "Bater ponto",
                      onPressed: () async {
                        ponto.value = await SERVICE.baterPonto(
                          SERVICE.token,
                          -5.888,
                          -35.202,
                        );
                        Timer(Duration(seconds: 5), () => ponto.value = []);
                      },
                    ),
                    ponto.value.isNotEmpty
                        ? Container(
                            width: double.infinity,
                            height: height * 0.1,
                            decoration: BoxDecoration(
                              gradient: LinearGradient(
                                colors: [
                                  GetColor.blueLigth.color,
                                  GetColor.blueLigthAlfa.color,
                                ],
                              ),
                            ),
                            child: Row(
                              mainAxisAlignment: MainAxisAlignment.spaceAround,
                              children: [
                                Text(
                                  "${ponto.value[0]}",
                                  style: Theme.of(context).textTheme.labelLarge,
                                ),
                                Text(
                                  formatarData(ponto.value[1]),
                                  style: Theme.of(context).textTheme.labelLarge,
                                ),
                              ],
                            ),
                          )
                        : SizedBox(
                            width: double.infinity,
                            height: height * 0.1,
                          ),
                  ],
                ),
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(20.0),
              child: Image.asset("./images/ufrn-logo.png", width: width * 0.2),
            ),
          ],
        ),
      ),
    );
  }
}
