import os
import ast
import re
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'
)
logger = logging.getLogger(__name__)


class ImportConverter:
    def __init__(self, base_dir: str, package_name: str):
        self.base_dir = os.path.abspath(base_dir)
        self.package_name = package_name
        self.valid_modules = self._get_valid_modules()

    def _get_valid_modules(self) -> set:
        """Build a set of valid module paths in the project."""
        valid_modules = set()
        for root, _, files in os.walk(self.base_dir):
            for file in files:
                if file.endswith('.py'):
                    # Get relative path and convert to module format
                    rel_path = os.path.relpath(root, self.base_dir)
                    if rel_path == '.':
                        module_name = os.path.splitext(file)[0]
                    else:
                        module_name = f"{rel_path.replace(os.sep, '.')}.{os.path.splitext(file)[0]}"
                    valid_modules.add(module_name)
                    # Also add the directory as a valid module if it has __init__.py
                    if file == '__init__.py':
                        valid_modules.add(rel_path.replace(os.sep, '.'))
        logger.info("Valid project modules found:")
        for module in sorted(valid_modules):
            logger.info(f"  - {module}")
        return valid_modules

    def is_project_module(self, import_name: str) -> bool:
        """Check if the import corresponds to an actual project module."""
        # Remove the package prefix if it exists
        if import_name.startswith(f"{self.package_name}."):
            import_name = import_name[len(f"{self.package_name}."):]

        # Check if it's in our valid modules
        return import_name in self.valid_modules

    def get_python_files(self):
        """Recursively find all Python files in the project."""
        python_files = []
        for root, _, files in os.walk(self.base_dir):
            for file in files:
                if file.endswith('.py'):
                    python_files.append(os.path.join(root, file))
        return python_files

    def get_relative_path(self, file_path):
        """Get the relative path from base_dir to the file."""
        return os.path.relpath(file_path, self.base_dir)

    def convert_relative_to_absolute(self, import_stmt: str, current_file_path: str):
        """Convert a relative import statement to an absolute import."""
        match = re.match(r'from (\.+)(.*?) import (.*)', import_stmt)
        if not match:
            return import_stmt

        dots, rel_path, names = match.groups()
        current_rel_path = self.get_relative_path(current_file_path)
        current_parts = os.path.dirname(current_rel_path).split(os.sep)

        if dots:
            levels = len(dots)
            if levels <= len(current_parts):
                new_path = '.'.join(current_parts[:-levels])
                if rel_path:
                    new_path = f"{new_path}.{rel_path.replace('/', '.')}"
                absolute_import = f"from {self.package_name}.{new_path} import {names}"
                return absolute_import.strip()

        return import_stmt

    def process_file(self, file_path):
        """Process a single Python file and convert its imports."""
        try:
            with open(file_path, 'r') as f:
                content = f.read()

            tree = ast.parse(content)
            lines = content.splitlines()
            modified_lines = lines.copy()
            changes_made = False
            imports_found = 0

            for node in ast.walk(tree):
                if isinstance(node, (ast.ImportFrom, ast.Import)):
                    line_no = node.lineno - 1
                    original_line = lines[line_no].strip()

                    imports_found += 1
                    logger.info(f"\nFound import in {os.path.basename(file_path)}:")
                    logger.info(f"Original: {original_line}")

                    new_line = self.convert_relative_to_absolute(original_line, file_path)
                    logger.info(f"Converted: {new_line}")

                    if new_line != original_line:
                        modified_lines[line_no] = new_line
                        changes_made = True

            if imports_found == 0:
                logger.info(f"No local imports found in {os.path.basename(file_path)}")

            return changes_made, modified_lines

        except Exception as e:
            logger.error(f"Error processing {file_path}: {str(e)}")
            return False, []

    def update_files(self, dry_run=True):
        """Update all Python files in the project."""
        python_files = self.get_python_files()
        files_with_changes = 0
        total_files = len(python_files)

        logger.info(f"\nFound {total_files} Python files to process")

        for file_path in python_files:
            logger.info(f"\nProcessing: {file_path}")
            changes_made, modified_lines = self.process_file(file_path)

            if changes_made:
                files_with_changes += 1
                if dry_run:
                    logger.info(f"\nChanges needed for: {file_path}")
                    logger.info("Full file after changes would be:")
                    logger.info('-' * 50)
                    logger.info('\n'.join(modified_lines))
                    logger.info('-' * 50)
                else:
                    with open(file_path, 'w') as f:
                        f.write('\n'.join(modified_lines))
                    logger.info(f"Modified: {file_path}")

        logger.info(f"\nSummary:")
        logger.info(f"Total files processed: {total_files}")
        logger.info(f"Files requiring changes: {files_with_changes}")

    def cleanup_duplicate_imports(self, dry_run=True):
        """Clean up duplicate package prefixes in import statements."""
        python_files = self.get_python_files()
        files_with_changes = 0
        total_files = len(python_files)

        logger.info(f"\n=== Cleaning up duplicate imports ===")
        logger.info(f"Found {total_files} Python files to process")

        duplicate_pattern = rf"{self.package_name}\.{self.package_name}\."

        for file_path in python_files:
            try:
                with open(file_path, 'r') as f:
                    content = f.read()

                # Parse the file to properly handle imports
                tree = ast.parse(content)
                lines = content.splitlines()
                modified_lines = lines.copy()
                changes_made = False

                for node in ast.walk(tree):
                    if isinstance(node, (ast.ImportFrom, ast.Import)):
                        line_no = node.lineno - 1
                        original_line = lines[line_no]

                        # Check for duplicate package prefixes
                        if re.search(duplicate_pattern, original_line):
                            # Get the module path without the duplicate prefix
                            fixed_line = re.sub(duplicate_pattern, f"{self.package_name}.", original_line)

                            # Extract the module name and verify it's a project module
                            module_match = re.match(r'from (.*?) import|import (.*?)$', fixed_line)
                            if module_match:
                                module_name = next(filter(None, module_match.groups()))
                                module_name = module_name.split()[0]

                                if self.is_project_module(module_name):
                                    logger.info(f"\nIn file: {os.path.basename(file_path)}")
                                    logger.info(f"Original: {original_line.strip()}")
                                    logger.info(f"Changed to: {fixed_line.strip()}")
                                    modified_lines[line_no] = fixed_line
                                    changes_made = True
                                else:
                                    logger.warning(f"Skipping non-project import: {original_line.strip()}")

                if changes_made:
                    files_with_changes += 1
                    if not dry_run:
                        with open(file_path, 'w') as f:
                            f.write('\n'.join(modified_lines))
                        logger.info(f"Fixed imports in: {file_path}")

            except Exception as e:
                logger.error(f"Error processing {file_path}: {str(e)}")
                continue

    def cleanup_incorrect_package_imports(self, dry_run=True):
        """Clean up incorrectly prefixed external package imports."""
        python_files = self.get_python_files()
        files_with_changes = 0
        total_files = len(python_files)

        logger.info(f"\n=== Cleaning up incorrect package imports ===")
        logger.info(f"Found {total_files} Python files to process")

        # Common external packages that should never have 'ingest.' prefix
        external_packages = {
            'pandas', 'numpy', 'arcpy', 'arcgis', 'os', 'sys', 'datetime',
            'json', 'logging', 're', 'typing', 'collections', 'pathlib', 'time',
            'networkx', 'geopandas', 'math', 'configparser', 'shapely', 'itertools',
            'dask', 'io', 'shutil', 'psycopg2', 'random', 'osgeo', 'subprocess', 'pyogrio',
            'matplotlib', 'seaborn', 'sklearn',
        }

        for file_path in python_files:
            try:
                with open(file_path, 'r') as f:
                    content = f.read()

                tree = ast.parse(content)
                lines = content.splitlines()
                modified_lines = lines.copy()
                changes_made = False

                for node in ast.walk(tree):
                    if isinstance(node, (ast.ImportFrom, ast.Import)):
                        line_no = node.lineno - 1
                        original_line = lines[line_no]

                        # Check for incorrectly prefixed external packages
                        for pkg in external_packages:
                            pattern = rf"{self.package_name}\.{pkg}\b"
                            if re.search(pattern, original_line):
                                # Remove the incorrect prefix
                                fixed_line = re.sub(pattern, pkg, original_line)
                                logger.info(f"\nIn file: {os.path.basename(file_path)}")
                                logger.info(f"Original: {original_line.strip()}")
                                logger.info(f"Changed to: {fixed_line.strip()}")
                                modified_lines[line_no] = fixed_line
                                changes_made = True

                if changes_made:
                    files_with_changes += 1
                    if not dry_run:
                        with open(file_path, 'w') as f:
                            f.write('\n'.join(modified_lines))
                        logger.info(f"Fixed imports in: {file_path}")

            except Exception as e:
                logger.error(f"Error processing {file_path}: {str(e)}")
                continue

        logger.info(f"\nCleanup Summary:")
        logger.info(f"Total files processed: {total_files}")
        logger.info(f"Files fixed: {files_with_changes}")


if __name__ == "__main__":
    PROJECT_PATH = r"D:\Code\edh-to-3dhp-ingest"

    converter = ImportConverter(
        base_dir=PROJECT_PATH,
        package_name="ingest"
    )

    logger.info("\n=== Performing cleanup dry runs ===")
    logger.info("\n1. Checking for duplicate 'ingest.ingest' patterns...")
    converter.cleanup_duplicate_imports(dry_run=True)

    logger.info("\n2. Checking for incorrect package imports...")
    converter.cleanup_incorrect_package_imports(dry_run=True)

    response = input("\nDo you want to apply these changes? (y/n): ")
    if response.lower() == 'y':
        logger.info("\n=== Applying cleanups ===")
        converter.cleanup_duplicate_imports(dry_run=False)
        converter.cleanup_incorrect_package_imports(dry_run=False)
        logger.info("All cleanups completed successfully!")
    else:
        logger.info("Operation cancelled")
