import 'package:http/http.dart' as http;
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'dart:convert';

class Service {
  String _user;

  Service({String user = ""}) : _user = user;

  Future<String> login() async {
    try {
      var url = dotenv.env['URL'];
      var urlHttp = Uri.parse(url as String);
      var res = await http.post(urlHttp, body: {'username': _user});
      if (res.statusCode == 200) {
        var decode = jsonDecode(res.body);
        return decode["token"];
      } else {
        return "";
      }
    } catch (error) {
      // ignore: avoid_print
      print("Error $error");
      return "";
    }
  }

  static Future<List<dynamic>> baterPonto(
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

  static Future<bool> logout(String username, String tokenUser) async {
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

  static Future<List<dynamic>> pontosRelatorio(String tokenUser) async {
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
