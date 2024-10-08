import dataclasses

import numpy as np


@dataclasses.dataclass
class HistogramL2:
    """
    This class collects multiple HistogramL1B classes into one L2 per observational day.

    flight_software_version
    number_of_l1b_files_used: int
        number of good-time Level-1B files used for generation of Level-2 data
    number_of_all_l1b_files
      number of all Level-1B files for observational day
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
    filter_temperature_std_dev
        standard deviation for filter temperature [Celsius deg]
    hv_voltage_average
        observational-day-averaged channeltron voltage [volt]
    hv_voltage_std_dev
        standard deviation for channeltron voltage [volt]
    spin_period_average
        observational-day-averaged spin period [s] (onboard value)
    spin_period_std_dev
        a standard deviation for spin period [s]
    pulse_length_average
        observational-day-averaged pulse length [μs]
    pulse_length_std_dev
        standard deviation for pulse length [μs]
    spin_period_ground_average
        observational-day-averaged spin period [s] (ground value)
    spin_period_ground_std_dev
        a standard deviation for spin period [s]
    position_angle_offset_average
        observational-day-averaged GLOWS angular offset [deg]
    position_angle_offset_std_dev
        standard deviation for GLOWS angular offset [seg]
    spin_axis_orientation_std_dev
        standard deviation for spin-axis longitude and latitude [deg]
    spacecraft_location_std_dev
        standard deviation for ecliptic coordinates [km] of IMAP
    spacecraft_velocity_std_dev
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
    number_of_l1b_files_used: int
    number_of_all_l1b_files: int
    identifier: int #?
    start_time: np.double
    end_time: np.double
    daily_lightcurve: np.ndarray
    filter_temperature_average: np.double
    filter_temperature_std_dev: np.double
    hv_voltage_average: np.double
    hv_voltage_std_dev: np.double
    spin_period_average: np.double
    spin_period_std_dev: np.double
    pulse_length_average: np.double
    pulse_length_std_dev: np.double
    spin_period_ground_average: np.double
    spin_period_ground_std_dev: np.double
    position_angle_offset_average: np.double
    position_angle_offset_std_dev: np.double
    spin_axis_orientation_std_dev: np.double
    spacecraft_location_std_dev: np.double
    spacecraft_velocity_std_dev: np.double
    spin_axis_orientation_average: np.double
    spacecraft_location_average: np.double
    spacecraft_velocity_average: np.double
    bad_time_flag_occurrences: np.ndarray