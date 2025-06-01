VaultCrypt – A Secure, Encrypted Password Manager in Python

VaultCrypt is a minimalist yet robust password manager built with Python and Fernet symmetric encryption from the cryptography module. Designed with privacy and simplicity in mind, it leverages local encryption, master-key authentication, and a secure key storage mechanism to keep your credentials safe, all while remaining lightweight and fully offline.

Features
Fernet Encryption (AES 128)
All credentials are encrypted using symmetric key encryption, ensuring confidentiality even if the password file is compromised.

Master Key Authentication
Users are required to authenticate with a master key. The master key itself is encrypted and stored securely.

Key Management System
Generates and securely stores a unique encryption key (key.key) for each instance on first use.

Command-Line Interface (CLI)
A simple and intuitive terminal interface to add, view, and manage encrypted credentials.

Local-Only Storage
No internet dependencies — 100% offline, ensuring sensitive data remains on your machine.
