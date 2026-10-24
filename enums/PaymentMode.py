"""
package org.nailyourinterview.lld.parking_lot.enums;

public enum PaymentMode {
    CASH,
    CARD,
    UPI
}
"""

from enum import Enum

class PaymentMode(Enum):
    CASH = "cash"
    CARD = "card"
    UPI = "upi"