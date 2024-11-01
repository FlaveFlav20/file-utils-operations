use pyo3::prelude::*;

use regex::Regex;
use std::collections::VecDeque;
use std::fs::read_to_string;

use crate::utils::convert_queue_to_vec;

#[pyclass]
pub struct WithEOL {}

#[pymethods]
impl WithEOL {
    #[staticmethod]
    #[pyo3(signature = (file, n, remove_empty_string=false, keep_when_regex=false, pass_when_regex=false, regex="".to_string()))]
    pub fn head(
        file: String,
        n: usize,
        remove_empty_string: bool,
        keep_when_regex: bool,
        pass_when_regex: bool,
        regex: String,
    ) -> Vec<String> {
        let mut result: Vec<String> = Vec::new();
        let re: Regex = Regex::new(&regex).unwrap();

        if n == 0 {
            return result;
        }

        for line in read_to_string(file).unwrap().lines() {
            if remove_empty_string && line.to_string().is_empty() {
                continue;
            } else if keep_when_regex && !re.is_match(line) {
                continue;
            } else if pass_when_regex && re.is_match(line) {
                continue;
            }
            result.push(line.to_string());
            if result.len() >= n {
                break;
            }
        }
        result
    }

    #[staticmethod]
    #[pyo3(signature = (file, n1, n2, remove_empty_string=false, keep_when_regex=false, pass_when_regex=false, regex="".to_string()))]
    pub fn between(
        file: String,
        n1: usize,
        n2: usize,
        remove_empty_string: bool,
        keep_when_regex: bool,
        pass_when_regex: bool,
        regex: String,
    ) -> Vec<String> {
        let mut result: Vec<String> = Vec::new();
        let re: Regex = Regex::new(&regex).unwrap();
        let mut counter: usize = 1;
        for line in read_to_string(file).unwrap().lines() {
            if remove_empty_string && line.to_string().is_empty() {
                continue;
            } else if keep_when_regex && !re.is_match(line) {
                continue;
            } else if pass_when_regex && re.is_match(line) {
                continue;
            }
            if counter > n2 {
                break;
            } else if counter >= n1 {
                result.push(line.to_string());
            }
            counter += 1;
        }
        result
    }

    #[staticmethod]
    #[pyo3(signature = (file, n, remove_empty_string=false, keep_when_regex=false, pass_when_regex=false, regex="".to_string()))]
    pub fn tail(
        file: String,
        n: usize,
        remove_empty_string: bool,
        keep_when_regex: bool,
        pass_when_regex: bool,
        regex: String,
    ) -> Vec<String> {
        let mut result: VecDeque<String> = VecDeque::with_capacity(n);
        let re: Regex = Regex::new(&regex).unwrap();
        if n == 0 {
            return convert_queue_to_vec(result);
        }

        for line in read_to_string(file).unwrap().lines() {
            if remove_empty_string && line.to_string().trim().is_empty() {
                continue;
            } else if keep_when_regex && !re.is_match(line) {
                continue;
            } else if pass_when_regex && re.is_match(line) {
                continue;
            }
            if result.len() == n {
                result.remove(0);
            }
            result.push_back(line.to_string());
        }

        convert_queue_to_vec(result)
    }

    #[staticmethod]
    #[pyo3(signature = (file, remove_empty_string=false, keep_when_regex=false, pass_when_regex=false, regex="".to_string()))]
    pub fn count_lines(
        file: String,
        remove_empty_string: bool,
        keep_when_regex: bool,
        pass_when_regex: bool,
        regex: String,
    ) -> usize {
        let mut res: usize = 0;
        let re: Regex = Regex::new(&regex).unwrap();
        for line in read_to_string(file).unwrap().lines() {
            if remove_empty_string && line.to_string().is_empty() {
                continue;
            } else if keep_when_regex && !re.is_match(line) {
                continue;
            } else if pass_when_regex && re.is_match(line) {
                continue;
            }
            res += 1;
        }
        res
    }
}
