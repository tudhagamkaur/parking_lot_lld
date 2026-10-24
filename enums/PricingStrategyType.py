"""
package org.nailyourinterview.lld.parking_lot.enums;

public enum PricingStrategyType {
    HOURLY,
    FLAT
}
"""

from enum import Enum

class PricingStrategyType(Enum):
    HOURLY = "hourly"
    FLAT = "flat"