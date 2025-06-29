import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:google_fonts/google_fonts.dart';
import 'dart:async';
import '../components/my_button.dart';
import '../service/service.dart';
import '../utils/format_date.dart';
import '../styles/colors.dart';

class TelaHome extends HookWidget {
  final ValueNotifier<String> tokenUser;
  final double width;
  final double height;
  final ValueNotifier<String> username;

  const TelaHome({
    super.key,
    required this.tokenUser,
    required this.width,
    required this.height,
    required this.username,
  });

  @override
  Widget build(BuildContext context) {
    var ponto = useState([]);

    return Scaffold(
      appBar: AppBar(
        title: Text("SIGPONTO"),
        leading: IconButton(
          icon: Icon(Icons.logout),
          onPressed: () async {
            var logout = await Service.logout(username.value, tokenUser.value);
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
                        var relatorios = await Service.pontosRelatorio(
                          tokenUser.value,
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
                        ponto.value = await Service.baterPonto(
                          tokenUser.value,
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
                                  style: TextStyle(
                                    fontFamily:
                                        GoogleFonts.poppins().fontFamily,
                                    fontWeight: FontWeight.bold,
                                  ),
                                ),
                                Text(
                                  formatarData(ponto.value[1]),
                                  style: TextStyle(
                                    fontFamily:
                                        GoogleFonts.poppins().fontFamily,
                                    fontWeight: FontWeight.bold,
                                  ),
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
