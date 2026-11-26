from typing import List, Dict, Any, Optional
from database.db_manager import get_pyqs, insert_pyq, record_pyq_attempt

class PYQManager:
    @staticmethod
    def get_questions(gate_paper: Optional[str] = None, year: Optional[int] = None, subject: Optional[str] = None) -> List[Dict[str, Any]]:
        return get_pyqs(gate_paper=gate_paper, year=year, subject=subject)

    @staticmethod
    def submit_attempt(pyq_id: int, selected_option: str, correct_option: str) -> Dict[str, Any]:
        is_correct = (selected_option.strip().upper() == correct_option.strip().upper())
        record_pyq_attempt(pyq_id, selected_option, is_correct)
        return {
            "is_correct": is_correct,
            "correct_option": correct_option,
            "selected_option": selected_option
        }
