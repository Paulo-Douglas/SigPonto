import 'package:http/http.dart' as http;
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'dart:convert';

class Service {
  String _user;

  Service({String user = ""}) : _user = user;

  // _login() {
  //   // ignore: avoid_print
  //   print(_user);
  // }

  Future<String> login() async {
    try {
      var url = dotenv.env['URL'];
      var urlHttp = Uri.parse(url as String);
      var res = await http.post(urlHttp, body: {'username': _user});
      var decode = jsonDecode(res.body);
      return decode["token"];
    } catch (error) {
      return " ";
    }
  }

  String get user {
    // ignore: avoid_print
    print(_user);
    return _user;
  }
}
