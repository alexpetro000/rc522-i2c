{
  "targets": [
    {
      "target_name": "rc522-i2c",
      "sources": [
        "src/rc522.c",
        "src/rfid.c",
        "src/accessor.cc"
      ],
      "libraries": [
        "-lbcm2835"
      ]
    }
  ]
}