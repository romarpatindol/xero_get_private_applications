# Xero Accounting GET API for Private Applications

A [Supercode](http://gosupercode.com) function that update values multiple request in one call google spreadsheet.
Still developing for other methods of google spreadsheet api.

## Server Usage

Get the Supercode Python SDK: https://git.io/vxTjp

```
import supercode
import pprint

credentials_json_data = {}
payload={}

response = supercode.call(
    "super-code-function",
    "your-supercode-api-key",
    consumer_key,
    rsa_key,
    query
)

pprint(response)
```

PyXero
======

PyXero is a Python API for accessing the REST API provided by the [Xero](https://developer.xero.com)
accounting tool. It allows access to both Public, Private and Partner applications.

### Private Applications

If using a Private application, you will need to install `PyCrypto`, a pure
Python cryptographic module. You'll also need to generate an signed RSA
certificate, and submit that certificate as part of registering your
application with Xero. See the [Xero Developer documentation](https://developer.xero.com/) for more
details.

When you [register your private application with Xero](https://developer.xero.com/documentation/auth-and-limits/private-applications/), you'll be given a
**Consumer Key**. You'll also be given a **Consumer secret** - this can be
ignored.

Using the Private credentials is much simpler than the Public credentials,
because there's no verification step -- verification is managed using RSA
signed API requests:

[Follow these steps](https://developer.xero.com/documentation/api-guides/create-publicprivate-key/) to generate a public/private key pair to sign your requests.  You'll upload your public key when you create your Xero Private app at https://app.xero.com.  You'll use the private key (aka RSA key) to generate your oAuth signature.

The RSA key is a multi-line string that will look something like::

    -----BEGIN RSA PRIVATE KEY-----
    MIICXgIBAAKBgQDWJbmxJjQLGM76sZkk2EhsdpV0Gxtrhzh/wiNBGffa5JHV/Ex4
    ....
    mtXGQjKqsOpuCw7HwgnRQUWKYbaJ3a+yTCFjVwa9keQhDQ==
    -----END RSA PRIVATE KEY-----

You can get this string by either reading the contents of your private key
file into a variable, or storing the key value as a constant. If you choose to
store the key value as a constant, remember two things:

* Make sure there is no leading space before
  the ``-----BEGIN PRIVATE KEY-----`` portion of the string.


## Query

```python
# Retrieve all contact objects
>>> query = "contacts.all()"
[{...contact info...}, {...contact info...}, {...contact info...}, ...]

# Retrieve a specific contact object
>>> query = "contacts.get('b2b5333a-2546-4975-891f-d71a8a640d23')"
{...contact info...}

# Retrive all contacts updated since 1 Jan 2013
>>> query = "contacts.filter(since=datetime(2013, 1, 1))"
[{...contact info...}, {...contact info...}, {...contact info...}]

# Retrive all contacts whose name is 'John Smith'
>>> query = "contacts.filter(Name='John Smith')"
[{...contact info...}, {...contact info...}, {...contact info...}]

# Retrive all contacts whose name starts with 'John'
>>> query = "contacts.filter(Name__startswith='John')"
[{...contact info...}, {...contact info...}, {...contact info...}]

# Retrive all contacts whose name ends with 'Smith'
>>> query = "contacts.filter(Name__endswith='Smith')"
[{...contact info...}, {...contact info...}, {...contact info...}]

# Retrive all contacts whose name starts with 'John' and ends with 'Smith'
>>> query = "contacts.filter(Name__startswith='John', Name__endswith='Smith')"
[{...contact info...}, {...contact info...}, {...contact info...}]

# Retrive all contacts whose name contains 'mit'
>>> query = "contacts.filter(Name__contains='mit')"
[{...contact info...}, {...contact info...}, {...contact info...}]
```

Complex filters can be constructed, for example retrieving invoices for a contact:

```python
>>> query = "invoices.filter(Contact_ContactID='83ad77d8-48a7-4f77-9146-e6933b7fb63b')"
```

Filters which aren't supported by this API can also be constructed using 'raw' mode like this:
```python
>>> query = "invoices.filter(raw='AmountDue > 0')"
```

Be careful when dealing with large amounts of data, the Xero API will take an
increasingly long time to respond, or an error will be returned. If a query might
return more than 100 results, you should make use of the ``page`` parameter::

```python
# Grab 100 invoices created after 01-01-2013
>>> query = "invoices.filter(since=datetime(2013, 1, 1), page=1)"
```

You can also order the results to be returned::

```python
# Grab contacts ordered by EmailAddress
>>> query = "contacts.filter(order='EmailAddress DESC')"
```

This same API pattern exists for the following API objects:

* Accounts
* Attachments
* BankTransactions
* BankTransfers
* BrandingThemes
* ContactGroups
* Contacts
* CreditNotes
* Currencies
* Employees
* ExpenseClaims
* Invoices
* Items
* Journals
* ManualJournals
* Organisation
* Overpayments
* Payments
* Prepayments
* Purchase Orders
* Receipts
* RepeatingInvoices
* Reports
* TaxRates
* TrackingCategories
* Users

**Note:** Supercode has not been launched yet. This is for internal testing only.
