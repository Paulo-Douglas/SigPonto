import 'package:flutter/material.dart';
import '../service/service.dart';

void loginSystemSubmmit(
  ValueNotifier<String> user,
  ValueNotifier<String> tokenUser,
  BuildContext context,
  String value,
  String rota,
) async {
  user.value = value;
  var token = await Service(user: user.value).login();
  tokenUser.value = token;

  if (tokenUser.value.isNotEmpty) {
    Navigator.pushNamed(context, rota);
  }
}

void loginSystemOnPressed(
  ValueNotifier<String> user,
  ValueNotifier<String> tokenUser,
  BuildContext context,
) async {
  var token = await Service(user: user.value).login();
  tokenUser.value = token;
  if (tokenUser.value.isNotEmpty) {
    Navigator.pushNamed(context, '/home');
  }
}
