# signal-cli - A python wrapper for the signal-cli-rest-api

### Documentation

The documentation of the code can be found here: https://fhune.de/signal_cli_documentation/

For the documentation of the signal-cli-rest-api, see <a href="https://github.com/bbernhard/signal-cli-rest-api">here</a>  (GitHub) and <a href="https://bbernhard.github.io/signal-cli-rest-api">here</a> (Swagger).

### Quick Start

* For using the module, you have to create a client object first: `signal_cli.Client(<address>, <port>, <phone_number>)`, with `address` and `port` building the access point to the signal-cli-rest-api and `number` building the phone number which should be used as client number.
* After creating the client object, you can use the other methods in their respective classes by passing the client object to the class object the method is in

### License

* _signal_cli_ is [![lgpl-3.0](https://img.shields.io/badge/license-lgpl__3__0-blue.svg)](LICENSE)

### Copyright

(c) 2022 Felix Hune
