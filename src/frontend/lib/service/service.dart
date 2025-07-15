import 'package:flutter/widgets.dart';
import 'package:http/http.dart' as http;
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'dart:convert';

// ignore: non_constant_identifier_names
var SERVICE = Service();

class Service {
  final ValueNotifier<Map<String, dynamic>> _credenciais =
      ValueNotifier<Map<String, dynamic>>({});
  final String _user;

  Service({String user = ""}) : _user = user;

  ValueNotifier<Map<String, dynamic>> get credenciaisNotifier => _credenciais;
  String get token => _credenciais.value["token"] ?? "";
  String get username => _credenciais.value["username"] ?? "";

  Future<void> login(String userName) async {
    try {
      var url = dotenv.env['URL'];
      var urlHttp = Uri.parse(url!);
      var res = await http.post(urlHttp, body: {'username': userName});
      if (res.statusCode == 200) {
        var decode = jsonDecode(res.body);
        _credenciais.value = decode;
      } else {
        // ignore: avoid_print
        print("Login falhou: ${res.statusCode}");
      }
    } catch (error) {
      // ignore: avoid_print
      print("Error $error");
    }
  }

  Future<List<dynamic>> baterPonto(
    String tokenUser,
    double latitude,
    double longitude,
  ) async {
    try {
      var url = dotenv.env['URL_PONTO'];
      var urlHttp = Uri.parse(url as String);
      var res = await http.post(
        urlHttp,
        headers: {
          'Authorization': 'Token $tokenUser',
          'Content-Type': 'application/json',
        },
        body: jsonEncode({'latitude': latitude, 'longitude': longitude}),
      );
      if (res.statusCode == 201) {
        var decode = jsonDecode(res.body);
        var ponto = [decode["tipo_ponto_display"], decode["data_hora"]];
        return ponto;
      } else {
        // ignore: avoid_print
        print("Erro ao bater ponto: ${res.statusCode}");
        return [];
      }
    } catch (error) {
      // ignore: avoid_print
      print("Error: $error");
      return [];
    }
  }

  Future<bool> logout(String username, String tokenUser) async {
    try {
      var url = dotenv.env['URL_LOGOUT'];
      var urlHttp = Uri.parse(url as String);
      var res = await http.post(
        urlHttp,
        headers: {
          'Authorization': 'Token $tokenUser',
          'Content-Type': 'application/json',
        },
        body: jsonEncode({'username': username}),
      );
      if (res.statusCode == 204) {
        return true;
      }
      return false;
    } catch (error) {
      // ignore: avoid_print
      print("Error: $error");
      return false;
    }
  }

  Future<List<dynamic>> pontosRelatorio(String tokenUser) async {
    try {
      var url = dotenv.env['URL_RELATORIO'];
      var urlHttp = Uri.parse(url as String);
      var res = await http.get(
        urlHttp,
        headers: {
          'Authorization': 'Token $tokenUser',
          'Content-Type': 'application/json',
        },
      );
      if (res.statusCode == 200) {
        var decode = jsonDecode(res.body);
        return decode;
      }
      return [];
    } catch (error) {
      // ignore: avoid_print
      print("Error: $error");
      return [];
    }
  }
}
