from enum import Enum, StrEnum


class ServiceFlags(StrEnum):
    ''' String values for ServiceFlags (array field) in GiactInquiry_5_9.
    Flags determine which service(s) to run on the inquiry.
    '''
    VERIFY = "verify"
    FUNDSCONFIRMATION = "fundsconfirmation"
    AUTHENTICATE = "authenticate"
    AUTHONLY = "authonly"
    VOIDEDCHECKIMAGE = "voidedcheckimage"
    IDENTIFYPERSON = "identifyperson"
    IDENTIFYPERSONKBA = "identifypersonkba"
    IDENTIFYBUSINESS = "identifybusiness"
    CUSTOMERIDPERSON = "customeridperson"
    CUSTOMERIDBUSINESS = "customeridbusiness"
    WORLDSANCTIONSCAN = "worldsanctionscan"
    ESI = "esi"
    DOMAINWHOIS = "domainwhois"
    MOBILEVERIFY = "mobileverify"
    MOBILEIDENTIFY = "mobileidentify"


class EnumWithDescription(Enum):
    def __new__(cls, value, description):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.description = description
        return obj


class VerificationResult_5_9(EnumWithDescription):
    ''' Values for VerificationResult field in GiactResult_5_9. Result is a
    summarized response of the combination of AccountResponseCode and
    CustomerResponseCode values.
    '''
    ERROR = (
        0,
        "There was an error with the inquiry. "
        "Check the ErrorMessage property for details.",
    )
    PRIVATEBADCHECKSLIST = (
        1,
        "The bank account in the inquiry was found on the API user's private "
        "bad check list.",
    )
    DECLINED = (
        2,
        "The suggested action is to decline the bank account and/or customer "
        "data for this inquiry.",
    )
    REJECTITEM = (
        3,
        "The suggested action is to not accept an item with the check number "
        "on this inquiry.",
    )
    ACCEPTWITHRISK = (
        4,
        "The suggested action is to further investigate or accept the bank "
        "account and/or customer data for this inquiry with known risk.",
    )
    RISKALERT = (
        5,
        "The suggested action is to further investigate the bank account "
        "and/or customer data for this inquiry due to a risk alert .",
    )
    PASS = (
        6,
        "The suggested action is to accept the bank account and/or customer "
        "data for this inquiry.",
    )
    PASSNDD = (
        7, "The bank account in the inquiry is a Non-Demand Deposit account."
    )
    NEGATIVEDATA = (
        8, "There was negative data found associated with the account."
    )
    NODATA = (
        9, "No data was found for the bank account and/or customer data."
    )


class AccountResponseCode(EnumWithDescription):
    ''' Values for ResponseCode field in AccountVerificationReply. Code
    indicates the current status of the account.
    '''
    NULL = (0, "There is no AccountResponseCode value for this result.")
    GS01 = (
        1,
        "Invalid Routing Number - The routing number supplied fails the "
        "validation test.",
    )
    GS02 = (
        2,
        "Invalid Account Number - The account number suplied fails the "
        "validation test.",
    )
    GS03 = (
        3,
        "Invalid Check Number - The check number supplied fails the "
        "validation test.",
    )
    GS04 = (
        4, "Invalid Amount - The amount supplied fails the validation test."
    )
    GP01 = (
        5, "The account was found as active in your Private Bad Checks List."
    )
    RT00 = (
        6,
        "The routing number belongs to a reporting bank; however, no positive "
        "nor negative information has been reported on the account number.",
    )
    RT01 = (
        7,
        "This account should be declined based on the risk factor being "
        "reported.",
    )
    RT02 = (
        8,
        "This item should be rejected based on the risk factor being reported."
    )
    RT03 = (
        9,
        "Current negative data exists on this account. Accept transaction "
        "with risk. (Example: Checking or savings accounts in NSF status, "
        "recent returns, or outstanding items)",
    )
    RT04 = (
        10,
        "Non-Demand Deposit Account (post no debits), Credit Card Check, Line "
        "of Credit, Home Equity, or a Brokerage check.",
    )
    RT05 = (11, "N/A")
    _1111 = (
        12,
        "Account Verified - The account was found to be an open and valid "
        "checking account.",
    )
    _2222 = (
        13,
        "AMEX - The account was found to be an American Express Travelers "
        "Cheque account.",
    )
    _3333 = (
        14,
        "Non-Participant Provider - This account was reported with "
        "acceptable, positive data found in current or recent transactions.",
    )
    _5555 = (
        15,
        "Savings Account Verified - The account was found to be an open "
        "and valid savings account.",
    )
    _7777 = (16, "N/A")
    _8888 = (17, "N/A")
    _9999 = (18, "N/A")
    GN01 = (19, "Negative information was found in this account's history.")
    GN05 = (
        20,
        "The routing number is reported as not currently assigned to a "
        "financial institution.",
    )
    ND00 = (
        21,
        "No positive or negative information has been reported on the account."
    )
    ND01 = (
        22,
        "This routing number can only be valid for US Government financial "
        "institutions.",
    )


class CustomerResponseCode(EnumWithDescription):
    ''' Values for ResponseCode field in AccountAuthenticationReply,
    PersonIdentificationReply and BusinessIdentificationReply.
    '''
    NULL = (
        0,
        "There is no CustomerResponseCode value for this result."
    )
    CA01 = (
        1,
        "Information submitted failed gAuthenticate."
    )
    CA11 = (
        2,
        "Customer authentication passed gAuthenticate."
    )
    CA21 = (
        3,
        "The customer or business name data did not match gAuthenticate "
        "data."
    )
    CA22 = (
        4,
        "The customer's TaxId (SSN/ITIN) data did not match gAuthenticate "
        "data."
    )
    CA23 = (
        5,
        "The customer's address data did not match gAuthenticate data."
    )
    CA24 = (
        6,
        "The customer's phone data did not match gAuthenticate data."
    )
    CA25 = (
        7,
        "The customer's date of birth or ID data did not match gAuthenticate "
        "data."
    )
    CA30 = (
        8,
        "Multiple secondary data points did not match gAuthenticate data."
    )
    CI01 = (
        9,
        "Information submitted failed gIdentify/CustomerID."
    )
    CI02 = (
        10,
        "N/A"
    )
    CI11 = (
        11,
        "Customer identification passed gIdentify/CustomerID."
    )
    CI21 = (
        12,
        "The customer or business name data did not match "
        "gIdentify/CustomerID data."
    )
    CI22 = (
        13,
        "The customer's TaxId (SSN/ITIN) data did not match "
        "gIdentify/CustomerID data."
    )
    CI23 = (
        14,
        "The customer's address data did not match gIdentify/CustomerID "
        "data."
    )
    CI24 = (
        15,
        "The customer's phone data did not match gIdentify/CustomerID "
        "data."
    )
    CI25 = (
        16,
        "The customer's date of birth or ID data did not match "
        "gIdentify/CustomerID data."
    )
    CI30 = (
        17,
        "Multiple secondary data points did not match gIdentify/CustomerID "
        "data."
    )
    ND02 = (
        18,
        "No data was found matching the customer information provided."
    )


class FundsConfirmationResult(EnumWithDescription):
    ''' Values for FundsConfirmatResult field in AccountVerificationReply.
    Result provides real-time indication of funds in the account.
    '''
    NULL = (
        0,
        "There is no FundsConfirmationResult value for this result."
    )
    NONPARTICIPATINGBANK = (
        1,
        "This item's bank is not a participant in the network."
    )
    INVALIDACCOUNTNUMBER = (
        2,
        "this item has an invalid account number."
    )
    ACCOUNTCLOSED = (
        3,
        "The bank is reporting this account as closed."
    )
    INSUFFICIENTFUNDS = (
        4,
        "There are not sufficient funds avaliable for this item's amount."
    )
    SUFFICENTFUNDS = (
        5,
        "There are sufficient funds avaliable for this item's amount."
    )


if __name__ == "__main__":
    print("Service Flags enumeration, v5.95, p25...")
    print(ServiceFlags.VERIFY)

    print("Verification result enumeration, v5.95, p39-38...")
    print(VerificationResult_5_9.PASS)
    print(VerificationResult_5_9.PASS.value)
    print(VerificationResult_5_9.PASS.description)

    print(
        "Account Verification Reply, "
        "AccountResponseCode enumeration, v5.95, p36..."
    )
    print(AccountResponseCode.GS01)
    print(AccountResponseCode.GS01.value)
    print(AccountResponseCode.GS01.description)
