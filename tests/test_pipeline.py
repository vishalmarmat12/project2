"""
Automated Pipeline & Deliverables Unit Test Suite
"""

import unittest
import os
import pandas as pd


class TestPortfolioPipeline(unittest.TestCase):
    
    def setUp(self):
        self.base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.data_dir = os.path.join(self.base_dir, "data")
        self.reports_dir = os.path.join(self.base_dir, "reports")
        self.vis_dir = os.path.join(self.base_dir, "visualizations")
        self.nb_dir = os.path.join(self.base_dir, "notebooks")
        self.pres_dir = os.path.join(self.base_dir, "presentation")
        
    def test_datasets_exist_and_healthy(self):
        datasets = [
            ("supermarket_sales.csv", 2000),
            ("student_performance.csv", 1000),
            ("weather_data.csv", 1000),
            ("healthcare_covid_trends.csv", 1000),
            ("real_estate_valuation.csv", 300)
        ]
        for filename, min_rows in datasets:
            path = os.path.join(self.data_dir, filename)
            self.assertTrue(os.path.exists(path), f"Missing dataset: {filename}")
            df = pd.read_csv(path)
            self.assertGreaterEqual(len(df), min_rows, f"Insufficient rows in {filename}")
            self.assertEqual(df.isnull().sum().sum(), 0, f"Unexpected nulls in {filename}")

    def test_pdf_reports_generated(self):
        reports = [
            "project1_supermarket_sales_report.pdf",
            "project2_student_performance_report.pdf",
            "project3_weather_data_report.pdf",
            "project4_healthcare_trends_report.pdf",
            "project5_real_estate_report.pdf",
            "portfolio_executive_summary.pdf"
        ]
        for r in reports:
            path = os.path.join(self.reports_dir, r)
            self.assertTrue(os.path.exists(path), f"Missing PDF report: {r}")
            self.assertGreater(os.path.getsize(path), 50000, f"PDF report suspiciously small: {r}")

    def test_visualizations_generated(self):
        for p in range(1, 6):
            p_dir = os.path.join(self.vis_dir, f"project{p}")
            self.assertTrue(os.path.exists(p_dir), f"Missing visualizations directory: project{p}")
            pngs = [f for f in os.listdir(p_dir) if f.endswith(".png")]
            self.assertGreaterEqual(len(pngs), 4, f"Project {p} has fewer than 4 charts")

    def test_notebooks_exist(self):
        for p in range(1, 6):
            nbs = [f for f in os.listdir(self.nb_dir) if f.startswith(f"0{p}")]
            self.assertEqual(len(nbs), 1, f"Missing notebook for project {p}")

    def test_presentation_exists(self):
        pptx_path = os.path.join(self.pres_dir, "portfolio_presentation.pptx")
        self.assertTrue(os.path.exists(pptx_path), "Missing presentation pptx")
        self.assertGreater(os.path.getsize(pptx_path), 20000, "Presentation pptx is too small")


if __name__ == "__main__":
    unittest.main()
