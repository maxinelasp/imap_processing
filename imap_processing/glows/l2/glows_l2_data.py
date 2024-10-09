import dataclasses

import numpy as np


@dataclasses.dataclass
class HistogramL2:
    """
    This class collects multiple HistogramL1B classes into one L2 per observational day.

    flight_software_version
    number_of_good_l1b_inputs: int
        number of good-time Level-1B times used for generation of Level-2 data
    total_l1b_inputs: int
      number of all Level-1B times for observational day
    identifier
        unique Level-2 histogram identifier
    start_time
        UTC start time of a given observational day
    end_time
        UTC end time of a given observational day
    daily_lightcurve
        arrays for observational-day-accumulated lightcurve
    filter_temperature_average
        observational-day-averaged filter temperature [Celsius deg]
    filter_temperature_variance
        standard deviation for filter temperature [Celsius deg]
    hv_voltage_average
        observational-day-averaged channeltron voltage [volt]
    hv_voltage_variance
        standard deviation for channeltron voltage [volt]
    spin_period_average
        observational-day-averaged spin period [s] (onboard value)
    spin_period_variance
        a standard deviation for spin period [s]
    pulse_length_average
        observational-day-averaged pulse length [μs]
    pulse_length_variance
        standard deviation for pulse length [μs]
    spin_period_ground_average
        observational-day-averaged spin period [s] (ground value)
    spin_period_ground_variance
        a standard deviation for spin period [s]
    position_angle_offset_average
        observational-day-averaged GLOWS angular offset [deg]
    position_angle_offset_variance
        standard deviation for GLOWS angular offset [seg]
    spin_axis_orientation_variance
        standard deviation for spin-axis longitude and latitude [deg]
    spacecraft_location_variance
        standard deviation for ecliptic coordinates [km] of IMAP
    spacecraft_velocity_variance
        standard deviation for IMAP velocity components [km/s]
    spin_axis_orientation_average
        observational-day-averaged spin-axis ecliptic longitude ⟨λ⟩ and lati- tude ⟨φ⟩ [deg]
    spacecraft_location_average
        observational-day-averaged Cartesian ecliptic coordinates ⟨X⟩, ⟨Y ⟩, ⟨Z⟩ [km] of IMAP
    spacecraft_velocity_average
        observational-day-averaged values ⟨VX ⟩, ⟨VY ⟩, ⟨VZ ⟩ of IMAP velocity components [km/s] (Cartesian ecliptic frame)
    bad_time_flag_occurrences
        numbers of occurrences of blocks for each bad-time flag during observational day
    """

    flight_software_version: str
    number_of_good_l1b_inputs: int
    total_l1b_inputs: int
    # identifier: int  # comes from unique_block_identifier
    start_time: np.double
    end_time: np.double
    daily_lightcurve: np.ndarray
    filter_temperature_average: np.double
    filter_temperature_variance: np.double
    hv_voltage_average: np.double
    hv_voltage_variance: np.double
    spin_period_average: np.double
    spin_period_variance: np.double
    pulse_length_average: np.double
    pulse_length_variance: np.double
    spin_period_ground_average: np.double
    spin_period_ground_variance: np.double
    position_angle_offset_average: np.double
    position_angle_offset_variance: np.double
    spin_axis_orientation_variance: np.double
    spacecraft_location_variance: np.double
    spacecraft_velocity_variance: np.double
    spin_axis_orientation_average: np.double
    spacecraft_location_average: np.double
    spacecraft_velocity_average: np.double
    bad_time_flag_occurrences: np.ndarray
